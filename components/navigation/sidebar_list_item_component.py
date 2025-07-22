from typing import Pattern
from playwright.sync_api import Page
import allure

from components.base_component import BaseComponent
from elements.icon import Icon
from elements.text import Text
from elements.button import Button


class SidebarListItemComponent(BaseComponent):
    def __init__(self, page: Page, identifier: str):
        super().__init__(page)

        self.icon = Icon(page, f'{identifier}-drawer-list-item-icon', 'Icon')
        self.title = Text(page, f'{identifier}-drawer-list-item-title-text', 'Title')
        self.button = Button(page,f'{identifier}-drawer-list-item-button', 'Button')

    @allure.step('Check visible "{title}" sidebar list item')
    def check_visibility(self, title: str):
        self.icon.check_visibility()

        self.title.check_visibility()
        self.title.check_have_text(title)

        self.button.check_visibility()

    def navigate(self, expected_url: Pattern[str]):
        self.button.click()
        self.check_current_url(expected_url)
