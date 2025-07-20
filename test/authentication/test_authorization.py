import pytest
from pages.authentication.login_page import LoginPage
from pages.authentication.registration_page import RegistrationPage
from pages.dashboard.dashboard_page import DashboardPage


@pytest.mark.regression
@pytest.mark.authorization
class TestAuthorization:
    def test_successful_authorization(
            self,
            login_page: LoginPage,
            dashboard_page: DashboardPage,
            registration_page: RegistrationPage
    ):
        registration_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')
        registration_page.registration_form.fill(email='user@gmail.com', username='username', password='pass')
        registration_page.registration_button.click()

        dashboard_page.toolbar_view.check_visibility()
        dashboard_page.navbar.check_visibility('username')
        dashboard_page.sidebar.check_visibility()
        dashboard_page.sidebar.click_logout()

        login_page.login_form.fill(email='user@gmail.com', password='pass')
        login_page.login_button.click()

        dashboard_page.toolbar_view.check_visibility()
        dashboard_page.navbar.check_visibility('username')
        dashboard_page.sidebar.check_visibility()


    @pytest.mark.parametrize("email, password", [
        ("user.name@gmail.com", "password"),
        ("user.name@gmail.com", "  "),
        ("  ", "password")
    ])
    def test_wrong_email_or_password_authorization(self, login_page: LoginPage, email: str, password: str):
        login_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login')
        login_page.login_form.fill(email=email, password=password)
        login_page.click_login_button()
        login_page.check_visibility_wrong_email_or_password_alert()

    def test_navigate_from_authorization_to_registration(
            self,
            login_page: LoginPage,
            registration_page: RegistrationPage
    ):
        login_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login')
        login_page.registration_link.click()

        registration_page.registration_form.check_visibility(email="", username="", password="")
