from film import Film
import os

class FilmSaver:

    def __init__(self, films: list[Film], website: str):
        self.films = films
        self.website = website

    def save(self) -> None:
        with open(f"films/{self.website}_films.txt", "w") as file:
            for film in self.films:
                file.write(f"{film}\n")

    def save_as_csv(self) -> None:
        file_path = f"films/{self.website}_films.csv"
        
        # Check if the file exists and if it is empty
        file_exists = os.path.exists(file_path)
        
        # Open the file in append mode
        with open(file_path, "a") as file:
            # If the file is empty, write the header
            if not file_exists or os.stat(file_path).st_size == 0:
                file.write("original_title;english_title;rating;year;film_poster;genres\n")
            
            # Write the film data
            for film in self.films:
                file.write(f"{film.to_csv()}\n")