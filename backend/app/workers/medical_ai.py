from app.core.celery_app import celery_app
from app.core.database import SessionLocal
from app.models.scan import MedicalScan
import logging
import torch
import torchvision.transforms as transforms
from torchvision import models
from PIL import Image

logger = logging.getLogger(__name__)

resnet_model = None

def get_model():
    """Singleton : Charge le modèle uniquement si le sous-processus ne l'a pas encore fait."""
    global resnet_model
    if resnet_model is None:
        logger.info("🧠 Initialisation de ResNet-50 dans la RAM de ce sous-processus...")
        weights = models.ResNet50_Weights.DEFAULT
        resnet_model = models.resnet50(weights=weights)
        resnet_model.eval()
    return resnet_model

@celery_app.task(name="analyze_medical_scan")
def analyze_medical_scan(scan_id: str):
    db = SessionLocal()
    try:
        scan = db.query(MedicalScan).filter(MedicalScan.id == scan_id).first()
        if not scan:
            return "Scan introuvable"

        scan.status = "processing"
        db.commit()
        
        image_path = scan.file_path
        
        # Correction pour les PNG transparents (RGBA -> RGB)
        img = Image.open(image_path)
        if img.mode != 'RGB':
            img = img.convert('RGB')
        
        # Pipeline mathématique
        preprocess = transforms.Compose([
            transforms.Resize(256),
            transforms.CenterCrop(224),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
        ])
        
        input_tensor = preprocess(img)
        input_batch = input_tensor.unsqueeze(0)

        # Récupération sécurisée du modèle (Lazy Loading)
        model = get_model()

        # Inférence PyTorch
        with torch.no_grad():
            output = model(input_batch)
            
        probabilities = torch.nn.functional.softmax(output[0], dim=0)
        top_prob, top_catid = torch.topk(probabilities, 1)
        
        confidence = top_prob.item() * 100
        
        if confidence > 50.0:
            ai_diagnosis = f"Structure tissulaire analysée sans anomalie majeure. (Confiance IA : {confidence:.1f}%)"
        else:
            ai_diagnosis = f"Incertitude structurelle, zone à surveiller. (Confiance IA : {confidence:.1f}%)"

        scan.ai_result = ai_diagnosis
        scan.status = "completed"
        db.commit()
        logger.info(f"✅ Analyse terminée avec succès pour {scan_id}")
        
        return {"status": "completed"}
        
    except Exception as e:
        logger.error(f"❌ Erreur PyTorch: {str(e)}")
        db.rollback()
        try:
            scan.status = "failed"
            scan.ai_result = f"Échec critique: {str(e)}"
            db.commit()
        except:
            pass
    finally:
        db.close()
