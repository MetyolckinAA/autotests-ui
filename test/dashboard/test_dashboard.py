import pytest
import allure
from allure_commons.types import Severity

from config import settings
from pages.dashboard.dashboard_page import DashboardPage
from tools.allure.tags import AllureTag
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from tools.routes import AppRoute


@pytest.mark.dashboard
@pytest.mark.regression
@allure.tag(AllureTag.REGRESSION, AllureTag.DASHBOARD)
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.DASHBOARD)
@allure.story(AllureStory.DASHBOARD)
@allure.parent_suite(AllureEpic.LMS)
@allure.suite(AllureFeature.DASHBOARD)
@allure.sub_suite(AllureStory.DASHBOARD)
class TestDashboard:
    @allure.title('Check displaying of dashboard page')
    @allure.severity(Severity.NORMAL)
    def test_dashboard_displaying(self, dashboard_page_with_state: DashboardPage):
        dashboard_page_with_state.visit(AppRoute.DASHBOARD)

        dashboard_page_with_state.sidebar.check_visibility()
        dashboard_page_with_state.navbar.check_visibility(settings.test_user.username)

        dashboard_page_with_state.students_chart_view.check_visibility('Students')
        dashboard_page_with_state.activities_chart_view.check_visibility('Activities')
        dashboard_page_with_state.courses_chart_view.check_visibility('Courses')
        dashboard_page_with_state.scores_chart_view.check_visibility('Scores')
