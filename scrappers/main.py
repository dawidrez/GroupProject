from film_saver import FilmSaver
from scrappers import FilmwebScraper

if __name__ == '__main__':
    scrapper = FilmwebScraper()
    scrapper.scrape()
    films = scrapper.get_films()
    saver = FilmSaver(films, "filmweb")
    saver.save()