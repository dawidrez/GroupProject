import pandas as pd


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


if __name__ == "__main__":
    imdb_csv_path = "films/imdb_films.csv"
    filmweb_csv_path = "films/filmweb_films.csv"
    missing_titles = find_missing_titles(imdb_csv_path, filmweb_csv_path)
    print("\nOriginal titles that are in IMDB but not in Filmweb:")
    for title in missing_titles:
        print(f"- {title}")
