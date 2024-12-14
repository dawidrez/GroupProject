import uuid
from typing import List, Optional

from pydantic import BaseModel


class GenreSchema(BaseModel):
    id: uuid.UUID
    name: str

    class Config:
        orm_mode = True
        from_attributes = True


class FilmSchema(BaseModel):
    id: uuid.UUID
    original_title: str
    english_title: Optional[str]
    year: int
    filmweb_rating: Optional[float]
    imdb_rating: Optional[float]
    genres: List[GenreSchema]
    src: str

    class Config:
        orm_mode = True
        from_attributes = True
