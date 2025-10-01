from fastapi import FastAPI
from app.routers import users
from app import models, database

models.Base.metadata.create_all(bind=database.engine)

# Cria a aplicação FastAPI
app = FastAPI(title="API de Usuários com FastAPI e SQLAlchemy")

# Inclui rotas de usuários
app.include_router(users.router, prefix="/users", tags=["users"])


