from abc import ABC, abstractmethod
from random import random
from time import sleep

from playwright.sync_api import sync_playwright


class Scraper(ABC):

    @abstractmethod
    def scrape(self):
        pass

    def random_wait(self):
        random_number = random.uniform(0.3, 0.8)
        sleep(random_number)


class FilmwebScraper(Scraper):

    url = "https://www.filmweb.pl/ranking/film"

    def initialize(self):
        self.pr = sync_playwright().start()
        self.browser = self.pr.firefox.launch()
        self.page = self.browser.new_page()
        self.page.goto(self.url)
        self.page.wait_for_event("load")


    def accept_cookies(self):
        self.random_wait()
        self.page.click("text=Akceptuję i przechodzę do serwisu")


    def scrape(self):
        self.initialize()
        self.accept_cookies()


FilmwebScraper().scrape()
