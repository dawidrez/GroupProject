import os

from dotenv import load_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

load_dotenv()

# Database URL from environment variables
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///films.db")

# Create SQLAlchemy engine and session factory
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Initialize SQLAlchemy object
db = SQLAlchemy()


def init_db(app: Flask) -> None:
    """Bind SQLAlchemy to the Flask app and create tables."""
    db.init_app(app)
    with app.app_context():
        db.create_all()
