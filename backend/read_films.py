import uuid
from enum import Enum

import pandas as pd
from app.models import Film, Genre
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URI = "postgresql://postgres:postgres@db:5432/app_db"

engine = create_engine(SQLALCHEMY_DATABASE_URI, echo=True)
Session = sessionmaker(bind=engine)


class Website(Enum):
    imdb = "imdb"


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
        film = session.query(Film).filter_by(original_title=row.original_title).first()
        if not film:
            continue
        if website == Website.imdb:
            print(film.original_title)
            film.imdb_rating = row["rating"]
            film.english_title = row["english_title"]
        session.merge(film)


if __name__ == "__main__":
    csv_filmweb = "filmweb_films.csv"
    csv_imdb = "imdb_films.csv"
    with Session() as session:
        load_films_from_filmweb(csv_filmweb)
        load_ratings_from_other_sites(csv_imdb, Website.imdb)
        session.commit()
