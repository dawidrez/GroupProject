from film import Film


class FilmSaver:

    def __init__(self, films: list[Film], website:str):
        self.films = films
        self.website = website

    def save(self) ->None:
        with open(f"films/{self.website}_films.txt", "w") as file:
            for film in self.films:
                file.write(f"{film}\n")

    def save_as_csv(self) -> None:
        with open(f"films/{self.website}_films.csv", "a") as file:
            file.write("original_title,english_title,rating,year\n")
            for film in self.films:
                file.write(f"{film.to_csv()}\n")
