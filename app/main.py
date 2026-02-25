from fastapi import FastAPI
from .routers import user

app = FastAPI(title="User Management SQLite")

app.include_router(user.router)

@app.get("/")
def root():
    return {"message": "User Management API Running"}