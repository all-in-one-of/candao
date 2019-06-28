import pytest
from selenium import webdriver
from page.login_page import LoginPage
from config.settings import browser
import time
import os
@pytest.fixture(scope="session")
def driver(request):
    if browser=='chrome':
        driver = webdriver.Chrome()
    elif browser=='firefox':
        driver = webdriver.Firefox()

    def end():
        driver.quit()
    request.addfinalizer(end) #addfinalizer的功能和yield一样，实现teardowm,区别是可以return 参数
    return driver

@pytest.fixture(scope="module")
def login(driver):
    driver.get("http://127.0.0.1:81/zentao/user-login-L3plbnRhby8=.html")
    LoginPage(driver).login()
