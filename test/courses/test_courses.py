import pytest
import allure
from allure_commons.types import Severity

from config import settings
from pages.courses.create_course_page import CreateCoursePage
from pages.courses.courses_list_page import CoursesListPage
from tools.allure.tags import AllureTag
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from tools.routes import AppRoute


@pytest.mark.courses
@pytest.mark.regression
@allure.tag(AllureTag.REGRESSION, AllureTag.COURSES)
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.COURSES)
@allure.story(AllureStory.COURSES)
@allure.parent_suite(AllureEpic.LMS)
@allure.suite(AllureFeature.COURSES)
@allure.sub_suite(AllureStory.COURSES)
class TestCourses:
    @allure.title('Check displaying of empty courses list')
    @allure.severity(Severity.NORMAL)
    def test_empty_courses_list(self, courses_list_page: CoursesListPage):
        courses_list_page.visit(AppRoute.COURSES)

        courses_list_page.navbar.check_visibility(settings.test_user.username)
        courses_list_page.sidebar.check_visibility()

        courses_list_page.toolbar_view.check_visibility()
        courses_list_page.check_visibility_empty_view()

    @allure.title('Test create course')
    @allure.severity(Severity.CRITICAL)
    def test_create_course(self, create_course_page: CreateCoursePage, courses_list_page: CoursesListPage):
        create_course_page.visit(AppRoute.CREATE_COURSE)

        create_course_page.create_course_toolbar_view.check_visibility(is_create_course_disabled=True)
        create_course_page.image_upload_widget.check_visibility(is_image_uploaded=False)
        create_course_page.create_course_form.check_visibility(
            title="",
            estimated_time="",
            description="",
            max_score="0",
            min_score="0"
        )

        create_course_page.create_course_exercise_toolbar_view.check_visibility()
        create_course_page.check_visibility_exercises_empty_view()

        create_course_page.image_upload_widget.upload_preview_image(file=settings.test_data.image_png_file)
        create_course_page.image_upload_widget.check_visibility(is_image_uploaded=True)

        create_course_page.create_course_form.fill(
            title="Playwright",
            description="Playwright",
            max_score="100",
            min_score="10",
            estimated_time="2 weeks")
        create_course_page.create_course_toolbar_view.click_create_course_button()

        courses_list_page.toolbar_view.check_visibility()
        create_course_page.course_view.check_visibility(
            index=0,
            title="Playwright",
            max_score="100",
            min_score="10",
            estimated_time="2 weeks"
        )

    @allure.title('Test edit course')
    @allure.severity(Severity.CRITICAL)
    def test_edit_course(self, create_course_page: CreateCoursePage, courses_list_page: CoursesListPage):
        create_course_page.visit(AppRoute.CREATE_COURSE)

        create_course_page.image_upload_widget.upload_preview_image(settings.test_data.image_png_file)
        create_course_page.image_upload_widget.check_visibility(is_image_uploaded=True)

        create_course_page.create_course_form.fill(
            title="Playwright",
            description="Playwright",
            max_score="100",
            min_score="10",
            estimated_time="2 weeks")
        create_course_page.create_course_toolbar_view.click_create_course_button()

        courses_list_page.toolbar_view.check_visibility()
        create_course_page.course_view.check_visibility(
            index=0,
            title="Playwright",
            max_score="100",
            min_score="10",
            estimated_time="2 weeks"
        )

        create_course_page.course_view.menu.menu_button.click()
        create_course_page.course_view.menu.edit_menu_button.click()

        create_course_page.create_course_form.fill(
            title="New title",
            description="New description",
            max_score="1000",
            min_score="100",
            estimated_time="4 weeks")
        create_course_page.create_course_toolbar_view.click_create_course_button()

        courses_list_page.toolbar_view.check_visibility()
        create_course_page.course_view.check_visibility(
            index=0,
            title="New title",
            max_score="1000",
            min_score="100",
            estimated_time="4 weeks"
        )

