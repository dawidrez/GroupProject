from app.models import Film
from database import SessionLocal


def get_all_films():
    """Fetch all films from the database."""
    with SessionLocal() as session:
        return session.query(Film).all()
