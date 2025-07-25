from playwright.sync_api import Page
import allure

from components.base_component import BaseComponent
from components.courses.course_view_menu_component import CourseViewMenuComponent
from elements.text import Text
from elements.image import Image


class CourseViewComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.menu = CourseViewMenuComponent(page)

        self.title = Text(page, 'course-widget-title-text', 'Title')
        self.image = Image(page, 'course-preview-image', 'Preview')
        self.max_score_text = Text(page, 'course-max-score-info-row-view-text', 'Max score')
        self.min_score_text = Text(page, 'course-min-score-info-row-view-text', 'Min score')
        self.estimated_time_text = Text(page, 'course-estimated-time-info-row-view-text', 'Estomated time')

    @allure.step('Check visible course view at index "{index}"')
    def check_visibility(self, index: int, title: str, max_score: str, min_score: str, estimated_time: str):
        self.image.check_visibility(nth=index)

        self.title.check_visibility(nth=index)
        self.title.check_have_text(title, nth=index)

        self.max_score_text.check_visibility(nth=index)
        self.max_score_text.check_have_text(f'Max score: {max_score}', nth=index)

        self.min_score_text.check_visibility(nth=index)
        self.min_score_text.check_have_text(f'Min score: {min_score}', nth=index)

        self.estimated_time_text.check_visibility(nth=index)
        self.estimated_time_text.check_have_text(f'Estimated time: {estimated_time}', nth=index)
