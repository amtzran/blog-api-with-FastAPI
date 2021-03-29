from fastapi import FastAPI
from . import models
from .database import engine
from .routers import blogs, users, authentication

app = FastAPI(
    title="Swopyn API",
    description="This is a very fancy project, with auto docs for the API and everything",
    version="1.0.0",
)

models.Base.metadata.create_all(engine)

app.include_router(authentication.router)
app.include_router(blogs.router)
app.include_router(users.router)
