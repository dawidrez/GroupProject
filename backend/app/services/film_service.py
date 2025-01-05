from app.models import Film
from database import SessionLocal
from sqlalchemy.orm import joinedload


def get_all_films() -> list[Film]:
    """Fetch all films from the database."""
    with SessionLocal() as session:
        return session.query(Film).options(joinedload(Film.genres)).all()
