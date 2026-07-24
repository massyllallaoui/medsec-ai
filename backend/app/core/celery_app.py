from celery import Celery
import os

redis_url = os.getenv("REDIS_URL", "redis://redis:6379/0")

celery_app = Celery(
    "worker",
    broker=redis_url,
    backend=redis_url,
    # C'EST LA LIGNE MAGIQUE : On dit à Celery de chercher les tâches dans ce dossier
    include=['app.workers.medical_ai'] 
)

celery_app.conf.task_routes = {"app.workers.*": "main-queue"}
