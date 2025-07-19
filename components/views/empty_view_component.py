from playwright.sync_api import Page, expect

from components.base_component import BaseComponent
from elements.icon import Icon
from elements.text import Text


class EmptyViewComponent(BaseComponent):
    def __init__(self, page: Page, identifier: str):
        super().__init__(page)

        self.icon = Icon(page, f'{identifier}-empty-view-icon', 'Icon')
        self.title = Text(page, f'{identifier}-empty-view-title-text', 'Title')
        self.description = Text(page, f'{identifier}-empty-view-description-text', 'Description')

    def check_visibility(self, title: str, description: str):
        self.icon.check_visibility()

        self.title.check_visibility()
        self.title.check_have_text(title)

        self.description.check_visibility()
        self.description.check_have_text(description)
