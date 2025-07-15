from pages.dashboard_page import DashboardPage
import pytest


@pytest.mark.dashboard
@pytest.mark.regression
def test_dashboard_displaying(dashboard_page_with_state: DashboardPage):
    dashboard_page_with_state.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard')
    dashboard_page_with_state.navbar.check_visibility('username')
    dashboard_page_with_state.check_visibility_dashboard_title()
    dashboard_page_with_state.check_visibility_courses_score_chart()
    dashboard_page_with_state.check_visibility_students_chart()
    dashboard_page_with_state.check_visibility_courses_score_chart()
    dashboard_page_with_state.check_visibility_activities_title_chart()


