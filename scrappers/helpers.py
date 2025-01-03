import pandas as pd
from film_saver import FilmSaver

from scrappers import FilmwebScraper, IMDBScraper

IMDB_CSV_PATH = "films/imdb_films.csv"
FILMWEB_CSV_PATH = "films/filmweb_films.csv"


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
    # fulfill_filmweb_csv()
    fulfill_imdb_csv()
