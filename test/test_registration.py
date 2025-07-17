from pages.registration_page import RegistrationPage
from pages.dashboard_page import DashboardPage


def test_successful_registration(registration_page: RegistrationPage, dashboard_page: DashboardPage):
    email = 'user@gmail.com'
    username = 'my user'
    password = 'password123'
    registration_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')
    registration_page.registration_form.fill(email, username, password)
    registration_page.click_registration_button()
    dashboard_page.check_visibility_dashboard_title()
