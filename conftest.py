import pytest
from selenium import webdriver
from data import MAIN_PAGE_URL,RESOLUTION,payload
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as Options
import requests



@pytest.fixture(params=['chrome', 'firefox'])
def driver(request):
    if request.param == 'firefox':
        options = Options()
        options.add_argument(f'-width={RESOLUTION[0]}')
        options.add_argument(f'-height={RESOLUTION[1]}')
        driver = webdriver.Firefox(options=options)
    elif request.param == 'chrome':
        options = ChromeOptions()
        options.add_argument(f'--window-size={RESOLUTION[0]},{RESOLUTION[1]}')
        driver = webdriver.Chrome(options=options)
    driver.get(MAIN_PAGE_URL)
    yield driver
    driver.quit()

@pytest.fixture()
def make_new_user():
    response = requests.post(f'{MAIN_PAGE_URL}api/auth/register', payload)
    token = response.json()['accessToken']
    yield response
    requests.delete(f'{MAIN_PAGE_URL}api/auth/user', headers={'Authorization': token})
