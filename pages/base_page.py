from playwright.sync_api import Page, expect
from typing import Pattern
import allure

from tools.logger import get_logger

logger = get_logger("BASE_PAGE")


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def visit(self, url: str):
        step = f'Opening the url "{url}"'

        with allure.step(step):
            logger.info(step)
            self.page.goto(url, wait_until='networkidle')

    def reload(self):
        step = f'Reloading page with url "{self.page.url}"'

        with allure.step(step):
            logger.info(step)
            self.page.reload(wait_until='domcontentloaded')

    def check_current_url(self, expect_url: Pattern[str]):
        step = f'Checking the current url matches pattern "{expect_url.pattern}"'

        with allure.step(step):
            logger.info(step)
            expect(self.page).to_have_url(expect_url)
