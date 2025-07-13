from playwright.sync_api import sync_playwright, expect
import pytest
from pages.create_course_page import CreateCoursePage
from pages.courses_list_page import CoursesListPage


@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(chromium_page_with_state):
    page = chromium_page_with_state
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

    courses_title = page.get_by_test_id("courses-list-toolbar-title-text")
    expect(courses_title).to_be_visible()
    expect(courses_title).to_have_text("Courses")

    courses_empty_view_icon = page.get_by_test_id("courses-list-empty-view-icon")
    expect(courses_empty_view_icon).to_be_visible()

    courses_empty_view_title = page.get_by_test_id("courses-list-empty-view-title-text")
    expect(courses_empty_view_title).to_be_visible()
    expect(courses_empty_view_title).to_have_text("There is no results")

    courses_empty_view_description = page.get_by_test_id("courses-list-empty-view-description-text")
    expect(courses_empty_view_description).to_be_visible()
    expect(courses_empty_view_description).to_have_text("Results from the load test pipeline will be displayed here")

    page.wait_for_timeout(4000)


@pytest.mark.courses
@pytest.mark.regression
def test_create_course(create_course_page: CreateCoursePage, courses_list_page: CoursesListPage):
    create_course_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create")

    create_course_page.check_visibility_create_course_title()
    create_course_page.check_disabled_create_course_button()
    create_course_page.check_visible_image_preview_empty_view()
    create_course_page.check_visibility_image_upload_view()
    create_course_page.check_visibility_create_course_form(
        title="",
        estimated_time="",
        description="",
        max_score="0",
        min_score="0"
    )
    create_course_page.check_visibility_exercises_title()
    create_course_page.check_visibility_create_exercise_button()
    create_course_page.check_visibility_exercises_empty_view()

    create_course_page.upload_preview_image(file='./testdata/files/image.png')
    create_course_page.check_visibility_image_upload_view()

    create_course_page.fill_create_course_form(
        title = "Playwright",
        estimated_time="2 weeks",
        description="Playwright",
        max_score="100",
        min_score="10"
    )
    create_course_page.click_create_course_button()

    courses_list_page.check_visibility_courses_title()
    courses_list_page.check_visibility_create_course_button()
    courses_list_page.check_visibility_course_card(
        index=0,
        title="Playwright",
        estimated_time="2 weeks",
        max_score="100",
        min_score="10"
    )
