import uuid

from sqlalchemy import Numeric
from sqlalchemy.orm import Mapped, declarative_base, mapped_column

Base = declarative_base()


class Film(Base):
    __tablename__ = "film"

    original_title: Mapped[str] = mapped_column(nullable=False, unique=True)
    english_title: Mapped[str | None] = mapped_column(nullable=True)
    year: Mapped[int] = mapped_column(nullable=False)
    filmweb_rating: Mapped[float] = mapped_column(Numeric(precision=2), nullable=False)
    imdb_rating: Mapped[float] = mapped_column(Numeric(precision=2), nullable=False)
    id: Mapped[uuid.UUID] = mapped_column(primary_key=True)
