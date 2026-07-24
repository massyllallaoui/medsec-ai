from sqlalchemy import Column, String, DateTime, ForeignKey, Boolean
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import uuid
from app.core.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    # LA CLÉ DE SÉCURITÉ : L'utilisateur appartient à UNE clinique. Si la clinique est supprimée (CASCADE), le user aussi.
    clinic_id = Column(UUID(as_uuid=True), ForeignKey("clinics.id", ondelete="CASCADE"), nullable=False)
    
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    is_admin = Column(Boolean, default=False) # True = Admin de la clinique
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    # Relation pour charger les infos de la clinique facilement depuis Python
    clinic = relationship("Clinic")
