from abc import ABC, abstractmethod
import random
from time import sleep

from playwright.sync_api import sync_playwright, ElementHandle

from film import Film


class Scraper(ABC):

    @abstractmethod
    def scrape(self) ->None:
        pass

    def random_wait(self) ->None:
        random_number = random.uniform(0.3, 0.8)
        sleep(random_number)


class FilmwebScraper(Scraper):

    url = "https://www.filmweb.pl/ranking/film"

    def __init__(self):
        self.pr = None
        self.browser = None
        self.page = None
        self.films = []

    def initialize(self) -> None:
        self.pr = sync_playwright().start()
        self.browser = self.pr.firefox.launch()
        self.context = self.browser.new_context(locale="en-GB", record_video_dir="records",
                                                record_video_size={"width": 3840, "height": 2160}, viewport={
                'width': 3840,  # Set the width of the viewport
                'height': 2160  # Set the height of the viewport
            })
        self.page = self.context.new_page()
        self.page.goto(self.url)
        self.page.wait_for_load_state("domcontentloaded")

    def close(self) -> None:
        self.page.close()
        self.browser.close()
        self.pr.stop()

    def accept_cookies(self) -> None:
        self.random_wait()
        self.page.click("xpath=//*[@id='didomi-notice-agree-button']")

    def convert_rating(self, rating: str) -> float:
        return float(rating.replace(",", "."))

    def scrape_film(self, selector: ElementHandle):
        film_card = selector.query_selector(".rankingType__card")

        film_genres = film_card.query_selector_all(".rankingGerne")
        genres = []

        for genre in film_genres:
            genres.append(genre.text_content())

        genres = ";".join(genres)

        original_title = film_card.query_selector(".rankingType__originalTitle").text_content()
        print(original_title)

        film_poster_src = selector.query_selector("div.efficientPoster img").get_attribute('src')

        original_title = film_card.query_selector(".rankingType__originalTitle").text_content()
        year = original_title[-4:]
        if original_title == year:
            film_name = film_card.query_selector(".rankingType__title").text_content().split(" ", 1)[1]
        else:
            film_name = original_title[:-5]
        film_rating = self.convert_rating(film_card.query_selector(".rankingType__rate--value").text_content())
        self.films.append(Film(original_title=film_name, english_title="", rating=film_rating, year=year, film_poster=film_poster_src, genres=genres))

    def scrape_films(self) -> None:
        selectors = self.page.query_selector_all(".rankingType")
        for selector in selectors:
            self.scrape_film(selector)

    def scroll_to_bottom(self) -> None:
        current_height = 0
        while True:
            height = self.page.evaluate("document.body.scrollHeight")
            while current_height < height:
                delta_y = random.randint(400, 600)
                self.page.mouse.wheel(delta_x=0, delta_y=delta_y)
                current_height += delta_y
                self.random_wait()
            new_height = self.page.evaluate("document.body.scrollHeight")
            if height == new_height:
                break

    def scrape(self) -> None:
        self.initialize()
        self.accept_cookies()
        self.scroll_to_bottom()
        self.scrape_films()
        self.close()

    def get_films(self) -> list[Film]:
        return self.films


class IMDBScraper(Scraper):

    url = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"




    def __init__(self):
        self.pr = None
        self.browser = None
        self.page = None
        self.films = []

    def initialize(self)->None:
        self.pr = sync_playwright().start()
        self.browser = self.pr.firefox.launch()
        self.context = self.browser.new_context(locale="en-GB", record_video_dir="records", record_video_size={"width": 3840, "height": 2160}, viewport={
                'width': 3840,  # Set the width of the viewport
                'height': 2160  # Set the height of the viewport
            })
        self.page = self.context.new_page()
        self.page.goto(self.url)
        self.page.wait_for_load_state("domcontentloaded")

    def close(self)->None:
        self.page.close()
        self.browser.close()
        self.pr.stop()


    def scrape_film(self, url: str)->None:
            self.random_wait()
            full_url = f"https://www.imdb.com{url}"
            self.page.goto(full_url)
            self.page.wait_for_load_state("domcontentloaded")
            self.page.screenshot(path=f"records/{self.page.title()}.png")
            information_selector = self.page.query_selector(".sc-70a366cc-0.bxYZmb")
            english_title =  information_selector.query_selector(".hero__primary-text").text_content()
            year = information_selector.query_selector(".ipc-link.ipc-link--baseAlt.ipc-link--inherit-color").text_content()
            try: 
                original_title = information_selector.query_selector(".sc-ec65ba05-1.fUCCIx").text_content()
                original_title = original_title[15:] # remove "Original title:"

            except Exception:
                original_title = english_title
            rating = self.page.query_selector(".sc-d541859f-1.imUuxf").text_content()
            self.films.append(Film(original_title=original_title, english_title=english_title, rating=float(rating), year=int(year)))

    def scrape_films(self)->None:
        selectors = self.page.query_selector_all(".sc-6ade9358-0.ktYEKX.cli-children")
        film_urls = []
        for selector in selectors:
            film_urls.append(selector.query_selector(".ipc-title-link-wrapper").get_attribute("href"))
        for url in film_urls:
            self.scrape_film(url)
        

    def scrape(self)->None:
        self.initialize()
        self.scrape_films()
        self.close()

    def get_films(self)->list[Film]:
        return self.films


