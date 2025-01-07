import pandas as pd
import os
from film_saver import FilmSaver

from scrappers import FilmwebScraper, IMDBScraper, MetacriticScrapper

IMDB_CSV_PATH = "films/imdb_films.csv"
FILMWEB_CSV_PATH = "films/filmweb_films.csv"
METACRITICS_CSV_PATH = "films/metacritics_films.csv"



def find_missing_titles(csv_path_1: str, csv_path_2: str) -> list[str]:
    """
    Read 2 CSV files and return a list of original titles
    that are in first CSV file but not in second CSV file

    Returns:
        list: List of original titles present in first CSV file but not in second CSV file
    """
    # Read both CSV files
    first_csv = pd.read_csv(csv_path_1, sep=";")
    second_csv = pd.read_csv(csv_path_2, sep=";")

    # Get sets of original titles from both dataframes
    first_titles = set(first_csv["original_title"])
    second_titles = set(second_csv["original_title"])

    # Find titles that are in first CSV but not in second CSV
    missing_titles = list(first_titles - second_titles)

    return missing_titles

def find_all_films(csv_path: str) -> list[str]:
    # Getting only imdb movies as for metacritics english title is required
    csv = pd.read_csv(csv_path, sep=";")

    titles = set(csv["english_title"])


    if os.path.exists(METACRITICS_CSV_PATH):
        metacritics_csv = pd.read_csv(METACRITICS_CSV_PATH, sep=";")
        metacritics_titles = set(metacritics_csv["original_title"])
    else:
        metacritics_titles = set()  

    missing_metacritics_titles = list(titles - metacritics_titles)

    return missing_metacritics_titles

def fulfill_metacritics_films() -> list[str]:
    missing_metacritics_titles = find_all_films(FILMWEB_CSV_PATH, IMDB_CSV_PATH)
    scrapper = MetacriticScrapper()
    scrapper.scrape_films_by_titles(missing_metacritics_titles)
    films = scrapper.get_films()
    saver = FilmSaver(films, "metacritics")
    saver.save_as_csv()


def fulfill_filmweb_csv():
    missing_titles = find_missing_titles(IMDB_CSV_PATH, FILMWEB_CSV_PATH)
    scraper = FilmwebScraper()
    scraper.scrape_films_by_titles(missing_titles)
    films = scraper.get_films()
    saver = FilmSaver(films, "filmweb")
    saver.save_as_csv()


def fulfill_imdb_csv():
    missing_titles = find_missing_titles(FILMWEB_CSV_PATH, IMDB_CSV_PATH)
    scraper = IMDBScraper()
    scraper.scrape_films_by_titles(missing_titles)
    films = scraper.get_films()
    saver = FilmSaver(films, "imdb")
    saver.save_as_csv()



if __name__ == "__main__":
    fulfill_filmweb_csv()
    fulfill_imdb_csv()
    # fulfill_metacritics_films()
