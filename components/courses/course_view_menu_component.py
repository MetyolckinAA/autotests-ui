from playwright.sync_api import Page
import allure

from components.base_component import BaseComponent
from elements.button import Button


class CourseViewMenuComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.menu_button = Button(page, 'course-view-menu-button', 'Menu')
        self.edit_menu_button = Button(page, 'course-view-edit-menu-item-text', 'Edit')
        self.delete_menu_button = Button(page, 'course-view-delete-menu-item-text', 'Delete')

    @allure.step('Open course menu at index "{index}" and click edit')
    def click_edit(self, index: int):
        self.menu_button.click(nth=index)

        self.menu_button.check_visibility(nth=index)
        self.edit_menu_button.click(nth=index)

    @allure.step('Open course menu at index "{index}" and click delete')
    def click_delete(self, index: int):
        self.menu_button.click(nth=index)

        self.delete_menu_button.check_visibility(nth=index)
        self.delete_menu_button.click(nth=index)
