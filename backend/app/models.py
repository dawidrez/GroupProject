import uuid

from sqlalchemy import ForeignKey, Numeric
from sqlalchemy.orm import Mapped, declarative_base, mapped_column, relationship

Base = declarative_base()


class FilmGenre(Base):
    __tablename__ = "film_genre"
    film_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("flm.id"), primary_key=True)
    genre_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("genre.id"), primary_key=True
    )


class Film(Base):
    __tablename__ = "film"

    original_title: Mapped[str] = mapped_column(nullable=False, unique=True)
    english_title: Mapped[str | None] = mapped_column(nullable=True)
    year: Mapped[int] = mapped_column(nullable=False)
    filmweb_rating: Mapped[float] = mapped_column(Numeric(precision=2), nullable=False)
    imdb_rating: Mapped[float] = mapped_column(Numeric(precision=2), nullable=False)
    id: Mapped[uuid.UUID] = mapped_column(primary_key=True)
    src: Mapped[str] = mapped_column(unique=True)

    genres: Mapped[list["Genre"]] = relationship(
        "Genre",
        secondary=FilmGenre,
    )


class Genre(Base):
    __tablename__ = "genre"
    id: Mapped[uuid.UUID] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(unique=True)
