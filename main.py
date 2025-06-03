from fastapi import FastAPI
from src.routes.user import user_router

app = FastAPI()

app.include_router(user_router)


@app.get("/")
def health_check():
    return {"health": "ok"}
