from fastapi import FastAPI
from routes.tracking import router as tracking_router
from database import Base, engine

app = FastAPI()


# Create the database tables
Base.metadata.create_all(bind=engine)


# Register API routes
app.include_router(tracking_router, prefix="/api")


@app.get("/")
def root():
    return {"message": "Welcome to the Carbon Footprint Tracker API"}
