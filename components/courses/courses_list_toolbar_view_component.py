import re

from components.base_component import BaseComponent
from playwright.sync_api import Page, expect
from elements.text import Text
from elements.button import Button


class CoursesListToolbarComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.title = Text(page, 'courses-list-toolbar-title-text', 'Title')
        self.create_course_button = Button(page, 'courses-list-toolbar-create-course-button', 'Button')

    def check_visibility(self):
        self.title.check_visibility()
        self.title.check_have_text('Courses')

        self.create_course_button.check_visibility()

    def click_create_course_button(self):
        self.create_course_button.click()
        self.check_current_url(re.compile('.*/#/courses/create'))



