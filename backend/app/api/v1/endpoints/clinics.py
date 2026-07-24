from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.clinic import ClinicRegister, ClinicResponse
from app.models.clinic import Clinic
from app.models.user import User
from app.core.security import get_password_hash

router = APIRouter()

@router.post("/register", response_model=ClinicResponse, status_code=status.HTTP_201_CREATED)
def register_clinic(payload: ClinicRegister, db: Session = Depends(get_db)):
    user_exists = db.query(User).filter(User.email == str(payload.admin_email)).first()
    if user_exists:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Cet email est déjà associé à un compte."
        )
    
    try:
        new_clinic = Clinic(
            name=payload.clinic_name,
            contact_email=str(payload.admin_email) # Forcer le format texte
        )
        db.add(new_clinic)
        db.flush() 

        new_admin = User(
            clinic_id=new_clinic.id,
            email=str(payload.admin_email),
            hashed_password=get_password_hash(payload.admin_password),
            is_admin=True
        )
        db.add(new_admin)
        
        db.commit()
        db.refresh(new_clinic)
        return new_clinic

    except Exception as e:
        db.rollback()
        # On renvoie l'erreur technique EXACTE au format texte pour le debug
        raise HTTPException(status_code=500, detail=f"Détail technique du crash : {str(e)}")
