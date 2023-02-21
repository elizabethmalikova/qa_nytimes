from playwright.sync_api import Playwright
from main_page import MainPage
from web_tests.settings.settings import *


class App:

    def __init__(self, playwright: Playwright, url: str):
        self.browser = playwright.chromium.launch(headless=headless_setting)
        self.context = self.browser.new_context()
        self.page = self.context.new_page()
        self.url = url
        self.page.goto(url)
        self.main_page = MainPage(self.page)

    def goto(self, endpoint: str, use_base_url=True):
        if use_base_url:
            self.page.goto(self.url + endpoint)
        else:
            self.page.goto(endpoint)
