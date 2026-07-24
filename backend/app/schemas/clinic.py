from pydantic import BaseModel, EmailStr
from uuid import UUID
from datetime import datetime

# Ce qu'on reçoit du frontend lors de l'inscription
class ClinicRegister(BaseModel):
    clinic_name: str
    admin_email: EmailStr
    admin_password: str

# Ce qu'on renvoie au frontend (On masque le mot de passe et on montre l'ID BDD)
class ClinicResponse(BaseModel):
    id: UUID
    name: str
    contact_email: EmailStr
    created_at: datetime

    class Config:
        from_attributes = True
