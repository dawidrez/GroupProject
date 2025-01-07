from app.models import Film
from database import SessionLocal
from sqlalchemy.orm import joinedload


def get_all_films() -> list[Film]:
    """Fetch all films from the database."""
    with SessionLocal() as session:
        return session.query(Film).options(joinedload(Film.genres)).all()


def get_paginated_films(
    page: int, per_page: int, genre_name: str | None = None, title: str | None = None
) -> tuple[list[Film], int]:
    """Fetch paginated films from the database with optional genre and title filtering."""
    with SessionLocal() as session:
        query = session.query(Film).options(joinedload(Film.genres))

        if genre_name:
            query = query.filter(Film.genres.any(name=genre_name))
        if title:
            query = query.filter(
                Film.original_title.ilike(f"%{title}%")
                | Film.english_title.ilike(f"%{title}%")
            )

        total_count = query.count()
        films = query.offset((page - 1) * per_page).limit(per_page).all()
        return films, total_count
