from components.charts.chart_view_component import ChartViewComponent
from components.dashboard.dashboard_toolbar_view_component import DashboardToolbarViewComponent
from components.navigation.navbar_component import NavbarComponent
from components.navigation.sidebar_component import SidebarComponent
from pages.base_page import BasePage
from playwright.sync_api import Page, expect


class DashboardPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.navbar = NavbarComponent(page)
        self.sidebar = SidebarComponent(page)
        self.toolbar_view = DashboardToolbarViewComponent(page)
        self.scores_chart_view = ChartViewComponent(page, "scores", "scatter")
        self.courses_chart_view = ChartViewComponent(page, "courses", "pie")
        self.students_chart_view = ChartViewComponent(page, "students", "bar")
        self.activities_chart_view = ChartViewComponent(page, "activities", "line")

        # self.students_title = page.get_by_test_id('students-widget-title-text')
        # self.students_chart = page.get_by_test_id('students-bar-chart')
        #
        # self.activities_title = page.get_by_test_id('activities-widget-title-text')
        # self.activities_chart = page.get_by_test_id('activities-line-chart')
        #
        # self.courses_title = page.get_by_test_id('courses-widget-title-text')
        # self.courses_chart = page.get_by_test_id('courses-pie-chart')
        #
        # self.scores_title = page.get_by_test_id('scores-widget-title-text')
        # self.scores_chart = page.get_by_test_id('scores-scatter-chart')

    # def check_visibility_students_chart(self):
    #     expect(self.students_title).to_be_visible()
    #     expect(self.students_title).to_have_text('Students')
    #     expect(self.students_chart).to_be_visible()
    #
    # def check_visibility_activities_title_chart(self):
    #     expect(self.activities_title).to_be_visible()
    #     expect(self.activities_title).to_have_text('Activities')
    #     expect(self.activities_chart).to_be_visible()
    #
    # def check_visibility_courses_score_chart(self):
    #     expect(self.scores_title).to_be_visible()
    #     expect(self.scores_title).to_have_text('Scores')
    #     expect(self.scores_chart).to_be_visible()
