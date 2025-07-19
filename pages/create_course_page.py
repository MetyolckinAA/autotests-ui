from playwright.sync_api import Page, expect

from components.courses.course_view_component import CourseViewComponent
from components.courses.create_course_exercise_form_component import CreateCourseExerciseFormComponent
from components.courses.create_course_exercises_toolbar_view_component import CreateCourseExercisesToolbarViewComponent
from components.courses.create_course_form_component import CreateCourseFormComponent
from components.courses.create_course_toolbar_view_component import CreateCourseToolbarViewComponent
from components.navigation.navbar_component import NavbarComponent
from components.views.empty_view_component import EmptyViewComponent
from components.views.image_upload_widget_component import ImageUploadWidgetComponent
from pages.base_page import BasePage
from elements.text import Text
from elements.button import Button


class CreateCoursePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.navbar = NavbarComponent(page)
        self.create_course_exercise_form = CreateCourseExerciseFormComponent(page)
        self.exercises_empty_view = EmptyViewComponent(page, 'create-course-exercises')
        self.image_upload_widget = ImageUploadWidgetComponent(page, 'create-course-preview')
        self.create_course_form = CreateCourseFormComponent(page)
        self.course_view = CourseViewComponent(page)
        self.create_course_toolbar_view = CreateCourseToolbarViewComponent(page)
        self.create_course_exercise_toolbar_view = CreateCourseExercisesToolbarViewComponent(page)

        self.exercises_title = Text(page, 'create-course-exercises-box-toolbar-title-text', 'Exercise title')
        self.create_exercise_button = Button(page, 'create-course-exercises-box-toolbar-create-exercise-button',
                                             'Create exercise button')

    def check_visibility_create_course_button(self):
        self.create_exercise_button.check_visibility()

    def check_visibility_exercises_empty_view(self):
        self.exercises_empty_view.check_visibility(
            title='There is no exercises',
            description='Click on "Create exercise" button to create new exercise'
        )
