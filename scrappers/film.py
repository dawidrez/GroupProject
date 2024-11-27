from dataclasses import dataclass


@dataclass
class Film:
    original_title: str
    english_title: str
    rating: float
    year: int

    def __str__(self) -> str:
        return f"{self.original_title} {self.year} - {self.rating}"

    def to_csv(self) -> str:
        return f"{self.original_title},{self.english_title},{self.rating},{self.year}"