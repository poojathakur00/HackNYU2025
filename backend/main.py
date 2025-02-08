from fastapi import FastAPI
from routes.tracking import router as tracking_router

app = FastAPI()

app.include_router(tracking_router, prefix="/api")


@app.get("/")
def root():
    return {"message": "Welcome to the Carbon Footprint Tracker API"}
