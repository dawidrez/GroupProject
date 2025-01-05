from app.models import Genre
from database import SessionLocal


def get_all_genres() -> list[Genre]:
    """Fetch all genres from the database."""
    with SessionLocal() as session:
        return session.query(Genre).all()
