from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.core.config import settings

# Création du pont entre FastAPI et PostgreSQL
engine = create_engine(settings.DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Fonction pour fournir une session BDD propre à chaque requête web
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
