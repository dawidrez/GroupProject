from dataclasses import dataclass
from typing import Optional


@dataclass
class Film:
    original_title: str
    english_title: str
    rating: float
    year: int
    film_poster: Optional[str] = None
    genres: Optional[str] = None

    def __str__(self) -> str:
        return f"{self.original_title} {self.year} - {self.rating}"

    def to_csv(self) -> str:
        return f"{self.original_title},{self.english_title},{self.rating},{self.year},{self.film_poster},{self.genres}"