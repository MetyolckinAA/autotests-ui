from playwright.sync_api import Page
import allure

from components.base_component import BaseComponent
from elements.text import Text


class NavbarComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.app_title = Text(page, 'navigation-navbar-app-title-text', 'App title')
        self.welcome_title = Text(page, 'navigation-navbar-welcome-title-text', 'Welcome title')

    @allure.step('Check visible navbar with username "{username}"')
    def check_visibility(self, username: str):
        self.app_title.check_visibility()
        self.app_title.check_have_text('UI Course')

        self.welcome_title.check_visibility()
        self.welcome_title.check_have_text(f'Welcome, {username}!')
