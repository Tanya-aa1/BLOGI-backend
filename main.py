from fastapi import FastAPI
from routers import auth_router, post_router
from fastapi.staticfiles import StaticFiles
from database import engine
import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth_router.router)
app.include_router(post_router.router)
app.mount("/static", StaticFiles(directory="static"), name="static")