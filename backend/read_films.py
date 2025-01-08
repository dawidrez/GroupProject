import uuid
from enum import Enum

import pandas as pd
from app.models import Film, Genre
from sqlalchemy import create_engine, or_
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URI = "postgresql://postgres:postgres@db:5432/app_db"

engine = create_engine(SQLALCHEMY_DATABASE_URI, echo=True)
Session = sessionmaker(bind=engine)
CSV_FILMWEB = "filmweb_films.csv"
CSV_IMDB = "imdb_films.csv"
CSV_METACRITIC = "metacritic_films.csv"


class Website(Enum):
    imdb = "imdb"
    metacritic = "metacritic"


def load_films_from_csv(csv_file_path: str) -> None:
    df = pd.read_csv(csv_file_path, delimiter=";")
    required_columns = {"original_title", "genres", "year", "rating", "film_poster"}
    if not required_columns.issubset(df.columns):
        raise ValueError(
            f"CSV file is missing required columns: {required_columns - set(df.columns)}"
        )
    for _, row in df.iterrows():
        genre_names = [name.strip() for name in row["genres"].split(",")]
        genres = []
        existing_genres = {g.name: g for g in session.query(Genre).all()}
        for name in genre_names:
            genre = existing_genres.get(name)
            if not genre:
                genre = Genre(name=name, id=uuid.uuid4())
                session.add(genre)
                existing_genres[name] = genre
            genres.append(genre)

        film = Film(
            id=uuid.uuid4(),
            original_title=row["original_title"],
            english_title=(
                row["english_title"] if pd.notna(row["english_title"]) else None
            ),
            year=row["year"],
            filmweb_rating=row["rating"],
            imdb_rating=None,
            genres=genres,
            src=row["film_poster"],
        )
        session.add(film)


def load_ratings_from_other_sites(csv_file_path: str, website: Website) -> None:
    df = pd.read_csv(csv_file_path, delimiter=";")

    for _, row in df.iterrows():
        film = (
            session.query(Film)
            .filter(
                or_(
                    Film.original_title.ilike(row.original_title),
                    Film.english_title.ilike(row.original_title),
                )
            )
            .first()
        )
        if not film:
            print(f"{row.original_title} not found")
            continue
        if website == Website.imdb:
            film.imdb_rating = row["rating"]
            film.english_title = row["english_title"]
        elif website == Website.metacritic:
            film.metacritic_rating = row["rating"]
        session.merge(film)


if __name__ == "__main__":
    with Session() as session:
        load_films_from_csv(CSV_FILMWEB)
        load_ratings_from_other_sites(CSV_IMDB, Website.imdb)
        load_ratings_from_other_sites(CSV_METACRITIC, Website.metacritic)
        session.commit()
