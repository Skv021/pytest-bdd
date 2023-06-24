import configparser

import pytest
from selenium import webdriver
import os


@pytest.fixture
def get_url():
    config = configparser.ConfigParser()
    config.read(r'config.ini')
    url = config['test']['url']
    #
    # print("++++++++++>>>>>>>>>",os.getcwd())
    # #print("------------>>>>>",os.path.dirname() )
    # config.read(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'config.ini'))
    # url = config['test']['url']
    return url


@pytest.fixture
def driver(get_url,get_pass):
    driver = webdriver.Chrome()
    driver.get(get_url)
    yield driver
    driver.quit()
