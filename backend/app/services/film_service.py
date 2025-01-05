from app.models import Film
from database import SessionLocal
from sqlalchemy.orm import joinedload


def get_all_films() -> list[Film]:
    """Fetch all films from the database."""
    with SessionLocal() as session:
        return session.query(Film).options(joinedload(Film.genres)).all()


def get_paginated_films(page: int, per_page: int) -> tuple[list[Film], int]:
    """Fetch paginated films from the database."""
    with SessionLocal() as session:
        query = session.query(Film)
        total_count = query.count()
        films = query.offset((page - 1) * per_page).limit(page).all()
        return films, total_count
