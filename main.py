from fastapi import FastAPI
from routes.api import router
from pymongo import MongoClient

def get_application() -> FastAPI:
    application = FastAPI()
    application.include_router(router)

    return application

app = get_application()

@app.get("/")
async def root():
    return {"message" : "MongoDB Sample Dataset - Sample_Analytics"}