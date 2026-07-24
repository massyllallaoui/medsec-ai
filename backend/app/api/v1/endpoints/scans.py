from fastapi import APIRouter, Depends, UploadFile, File, HTTPException, status
from sqlalchemy.orm import Session
import shutil
import os
from uuid import uuid4
from app.core.database import get_db
from app.models.user import User
from app.models.scan import MedicalScan
from app.api.deps import get_current_user
from app.workers.medical_ai import analyze_medical_scan

router = APIRouter()
UPLOAD_DIR = "/app/uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.post("/upload")
def upload_medical_scan(
    file: UploadFile = File(...), 
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    allowed_extensions = ('.png', '.jpg', '.jpeg', '.dcm', '.pdf')
    if not file.filename.lower().endswith(allowed_extensions):
        raise HTTPException(status_code=400, detail="Format non autorisé")
    
    clinic_dir = os.path.join(UPLOAD_DIR, str(current_user.clinic_id))
    os.makedirs(clinic_dir, exist_ok=True)
    
    file_extension = file.filename.split('.')[-1]
    secure_filename = f"{uuid4()}.{file_extension}"
    file_path = os.path.join(clinic_dir, secure_filename)
    
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
        
    new_scan = MedicalScan(
        clinic_id=current_user.clinic_id,
        original_filename=file.filename,
        file_path=file_path
    )
    db.add(new_scan)
    db.commit()
    db.refresh(new_scan)
    
    analyze_medical_scan.delay(str(new_scan.id))
    
    return {"message": "Image reçue", "scan_id": new_scan.id, "status": new_scan.status}

# NOUVELLE ROUTE : Le frontend l'appellera pour avoir le verdict
@router.get("/{scan_id}")
def get_scan_result(scan_id: str, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    scan = db.query(MedicalScan).filter(MedicalScan.id == scan_id, MedicalScan.clinic_id == current_user.clinic_id).first()
    if not scan:
        raise HTTPException(status_code=404, detail="Scan introuvable")
    return {"scan_id": scan.id, "status": scan.status, "ai_result": scan.ai_result}
