from film_saver import FilmSaver
from scrappers import FilmwebScraper, IMDBScraper

if __name__ == '__main__':
    scrapper = IMDBScraper()
    scrapper.scrape()
    films = scrapper.get_films()
    saver = FilmSaver(films, "imdb")
    saver.save_as_csv()