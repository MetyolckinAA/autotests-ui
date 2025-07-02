from playwright.sync_api import sync_playwright, expect


email = "user.name@gmail.com"
username = "username"
password = "password"


with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    login_email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    login_email_input.fill(email)

    username_input = page.get_by_test_id('registration-form-username-input').locator('input')
    username_input.fill(username)

    password_input = page.locator('//input[@type="password"]')
    password_input.fill(password)

    registration_button = page.get_by_test_id('registration-page-registration-button')
    registration_button.click()

    header = page.locator('//h6[text()="Dashboard"]')
    expect(header).to_be_visible()
