import pytest
from selene import browser
from selenium import webdriver


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    browser.config.base_url = 'https://demoqa.com/automation-practice-form'
    browser.config.window_height = 800
    browser.config.window_width = 600
    browser.config.timeout = 3

    yield

    browser.quit()
