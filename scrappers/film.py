from dataclasses import dataclass


@dataclass
class Film:
    name: str
    rating: float
    year: int

    def __str__(self) -> str:
        return f"{self.name} {self.year} - {self.rating}"