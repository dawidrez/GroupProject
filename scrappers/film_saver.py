from film import Film


class FilmSaver:

    def __init__(self, films: list[Film], website:str):
        self.films = films
        self.website = website

    def save(self) ->None:
        with open(f"films/{self.website}_films.txt", "w") as file:
            for film in self.films:
                file.write(f"{film}\n")
