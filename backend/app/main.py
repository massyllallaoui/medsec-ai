from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1.endpoints import clinics, auth, scans

app = FastAPI(title="MedSec AI API", version="1.0.0")

# --- LE VIGILE ANTI-CORS ---
# On autorise spécifiquement le frontend Next.js à faire des requêtes HTTP
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"], 
    allow_credentials=True,
    allow_methods=["*"], # Autorise POST, GET, PUT, DELETE...
    allow_headers=["*"], # Autorise l'envoi de Tokens JWT
)

app.include_router(auth.router, prefix="/api/v1/auth", tags=["Authentification"])
app.include_router(clinics.router, prefix="/api/v1/clinics", tags=["Clinics B2B"])
app.include_router(scans.router, prefix="/api/v1/scans", tags=["Imagerie Médicale"])

@app.get("/api/v1/health", tags=["Système"])
def health_check():
    return {"status": "online"}
