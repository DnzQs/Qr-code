from fastapi import FastAPI
from app.core.database import engine, Base
from app.qr.router import router as qr_router
from app.qr.models import QRHistory

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Welcome to QR Code Generator API! Go to /docs for Swagger UI."}