from sqlalchemy import Column, String, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
import uuid
from app.core.database import Base

class Clinic(Base):
    __tablename__ = "clinics"

    # UUID = Beaucoup plus sécurisé qu'un ID 1, 2, 3 (impossible à deviner pour un hacker)
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    contact_email = Column(String, nullable=False, unique=True)
    # On laisse PostgreSQL gérer l'heure exacte de création
    created_at = Column(DateTime(timezone=True), server_default=func.now())
