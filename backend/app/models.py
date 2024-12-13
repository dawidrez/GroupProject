import uuid

from sqlalchemy import Column, ForeignKey, Numeric, Table
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, declarative_base, mapped_column, relationship

Base = declarative_base()


film_genre_table = Table(
    "film_genre",
    Base.metadata,
    Column("film_id", UUID(as_uuid=True), ForeignKey("film.id"), primary_key=True),
    Column("genre_id", UUID(as_uuid=True), ForeignKey("genre.id"), primary_key=True),
)


class Film(Base):
    __tablename__ = "film"

    original_title: Mapped[str] = mapped_column(nullable=False, unique=True)
    english_title: Mapped[str | None] = mapped_column(nullable=True)
    year: Mapped[int] = mapped_column(nullable=False)
    filmweb_rating: Mapped[float] = mapped_column(Numeric(precision=2), nullable=True)
    imdb_rating: Mapped[float] = mapped_column(Numeric(precision=2), nullable=True)
    id: Mapped[uuid.UUID] = mapped_column(primary_key=True)
    src: Mapped[str] = mapped_column(unique=True)

    genres: Mapped[list["Genre"]] = relationship(
        "Genre",
        secondary=film_genre_table,  # Use Table here
    )


class Genre(Base):
    __tablename__ = "genre"
    id: Mapped[uuid.UUID] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(unique=True)
