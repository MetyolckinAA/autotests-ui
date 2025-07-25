from playwright.sync_api import Page
import allure

from components.base_component import BaseComponent
from elements.input import Input


class RegistrationFormComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.email_input = Input(page, 'registration-form-email-input', 'Email')
        self.username_input = Input(page, 'registration-form-username-input', 'Username')
        self.password_input = Input(page, 'registration-form-password-input', 'Password')

    @allure.step('Fill login form')
    def fill(self, email: str, username: str, password: str):
        self.email_input.fill(email)
        self.email_input.check_have_value(email)

        self.username_input.fill(username)
        self.username_input.check_have_value(username)

        self.password_input.fill(username)
        self.password_input.check_have_value(username)

    @allure.step('Check visible registration form')
    def check_visibility(self, email: str, username: str, password: str):
        self.email_input.check_visibility()
        self.email_input.check_have_value(email)

        self.username_input.check_visibility()
        self.username_input.check_have_value(username)

        self.password_input.check_visibility()
        self.password_input.check_have_value(password)
