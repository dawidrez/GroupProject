import uuid

import pandas as pd
from app.models import Film
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Database URI (example for PostgreSQL, modify based on your DB)
SQLALCHEMY_DATABASE_URI = "postgresql://postgres:postgres@db:5432/app_db"

# Set up the database engine and session
engine = create_engine(SQLALCHEMY_DATABASE_URI, echo=True)
Session = sessionmaker(bind=engine)
session = Session()


def load_films_from_csv(csv_file_path):
    # Read the CSV file
    df = pd.read_csv(csv_file_path)

    # Iterate over the DataFrame and insert each row into the database
    for _, row in df.iterrows():
        # Prepare the data to insert into the Film table
        film = Film(
            id=uuid.uuid4(),  # Generate a new UUID for each film
            original_title=row["original_title"],
            english_title=(
                row["english_title"] if pd.notna(row["english_title"]) else None
            ),
            year=row["year"],
            filmweb_rating=row["rating"],
            imdb_rating=None,
        )

        # Add the film instance to the session
        session.add(film)

    # Commit the transaction to the database
    session.commit()


# Run the import when the script is executed directly
if __name__ == "__main__":
    # Path to your CSV file
    csv_file_path = "../scrappers/films/filmweb_films.csv"

    try:
        load_films_from_csv(csv_file_path)
        print("Films imported successfully!")
    except Exception as e:
        print(f"Error importing films: {e}")
