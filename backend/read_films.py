import uuid

import pandas as pd
from app.models import Film, Genre
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URI = "postgresql://postgres:postgres@db:5432/app_db"

engine = create_engine(SQLALCHEMY_DATABASE_URI, echo=True)
Session = sessionmaker(bind=engine)
session = Session()


def load_films_from_csv(csv_file_path):
    df = pd.read_csv(csv_file_path, delimiter=";")

    for _, row in df.iterrows():
        genre_names = [name.strip() for name in row["genres"].split(",")]
        print(genre_names)
        genres = []
        for name in genre_names:
            genre = session.query(Genre).filter_by(name=name).first()
            if not genre:
                genre = Genre(name=name, id=uuid.uuid4())
                session.add(genre)
            genres.append(genre)

        print(f"genres!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!11 {genres}")
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
    session.commit()


if __name__ == "__main__":
    csv_file_path = "filmweb_films.csv"

    try:
        load_films_from_csv(csv_file_path)
        print("Films imported successfully!")
    except Exception as e:
        print(f"Error importing films: {e}")
