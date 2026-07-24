from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql://medsec_admin:supersecretpassword@db:5432/medsec_db"
    SECRET_KEY: str = "super-secret-key-pour-les-jwt"
    
settings = Settings()
