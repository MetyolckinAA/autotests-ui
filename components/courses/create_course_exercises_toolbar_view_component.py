from playwright.sync_api import Page
import allure

from components.base_component import BaseComponent
from elements.text import Text
from elements.button import Button


class CreateCourseExercisesToolbarViewComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.title = Text(page, 'create-course-exercises-box-toolbar-title-text', 'Title')
        self.create_button = Button(page, 'AddIcon', 'Create button')

    @allure.step('Check visible create course exercises toolbar view')
    def check_visibility(self):
        self.title.check_visibility()
        self.title.check_have_text('Exercises')

        self.create_button.check_visibility()

    def click_create_exercise_button(self):
        self.create_button.click()
