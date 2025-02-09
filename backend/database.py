from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime

# SQLite Database URL
DATABASE_URL = "sqlite:///./screen_time.db"

# Create database engine
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Session Local Class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base Model for SQLAlchemy
Base = declarative_base()

# Define the ScreenTimeEntry Table
class ScreenTimeEntry(Base):
    __tablename__ = "screen_time"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String, index=True)
    app_name = Column(String, index=True)
    duration = Column(Integer)  # Time in seconds
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)

# Create Tables in the Database
Base.metadata.create_all(bind=engine)
