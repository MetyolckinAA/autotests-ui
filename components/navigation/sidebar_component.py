from playwright.sync_api import Page
import re
import allure

from components.base_component import BaseComponent
from components.navigation.sidebar_list_item_component import SidebarListItemComponent


class SidebarComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.logout_list_item = SidebarListItemComponent(page, 'logout')
        self.courses_list_item = SidebarListItemComponent(page, 'courses')
        self.dashboard_list_item = SidebarListItemComponent(page, 'dashboard')

    @allure.step('Check visible sidebar')
    def check_visibility(self):
        self.logout_list_item.check_visibility('Logout')
        self.courses_list_item.check_visibility('Courses')
        self.dashboard_list_item.check_visibility('Dashboard')

    @allure.step('Click logout on sidebar')
    def click_logout(self):
        self.logout_list_item.navigate(re.compile(r".*/#/auth/login"))

    @allure.step('Click courses on sidebar')
    def click_courses(self):
        self.courses_list_item.navigate(re.compile(r".*/#/courses"))

    @allure.step('Click dashboard on sidebar')
    def click_dashboard(self):
        self.dashboard_list_item.navigate(re.compile(r".*/#/dashboard"))
