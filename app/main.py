from fastapi import FastAPI
from .routers import users, auth
from .database import SessionLocal, engine
from . import models

models.Base.metadata.create_all(bind=engine)
app = FastAPI()


# Routes:
app.include_router(users.router, tags=['Users'])
app.include_router(auth.router, tags=['Authentication'])