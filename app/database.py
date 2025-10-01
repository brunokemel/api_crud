from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.core.config import settings

# Criação do engine do banco de dados
engine = create_engine(
    settings.DATABASE_URL,
    echo=settings.DEBUG,  # Log das queries SQL em modo debug
    pool_pre_ping=True,   # Verifica conexões antes de usar
    pool_recycle=300      # Recicla conexões a cada 5 minutos
)

# Configuração da sessão
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para os modelos SQLAlchemy
Base = declarative_base()


def get_db():
    """
    Dependency que fornece uma sessão do banco de dados
    
    Yields:
        Session: Sessão do SQLAlchemy
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

