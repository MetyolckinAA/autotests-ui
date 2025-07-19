from playwright.sync_api import Page, expect

from components.base_component import BaseComponent
from elements.text import Text


class DashboardToolbarViewComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.title = Text(page, 'dashboard-toolbar-title-text', 'Title')

    def check_visibility(self):
        self.title.check_visibility()
        self.title.check_have_text('Dashboard')
