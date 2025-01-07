from film_saver import FilmSaver
from scrappers import FilmwebScraper, IMDBScraper, MetacriticScrapper

if __name__ == '__main__':
    # scrapper = IMDBScraper()
    scrapper = FilmwebScraper()
    scrapper.scrape_ranking()
    films = scrapper.get_films()
    # saver = FilmSaver(films, "imdb")
    saver = FilmSaver(films, "filmweb")
    saver.save_as_csv()