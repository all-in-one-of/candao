#coding:utf-8
from page.login_page import LoginPage
from selenium import webdriver
from util1.operater_xlsx import OperationExcel
import time
import pytest
from config.settings import url

class TestLogin:
    data = OperationExcel()
    login_sdata = data.get_sdata()
    login_fdata = data.get_fdata()
    print(login_sdata)
    print(login_fdata)

    @pytest.fixture(scope="function",autouse=True)
    def startpage(self,driver):
        driver.get(url)
        driver.delete_all_cookies()
        driver.refresh()

    @pytest.mark.fail
    @pytest.mark.parametrize("user,pwd", login_fdata)
    def test_login_fail(self,driver,user, pwd):
        page = LoginPage(driver)
        page.login(user, pwd)
        res = page.get_alert()
        print("测试结果：%s"% res)
        assert res

    @pytest.mark.success
    @pytest.mark.parametrize("user,pwd",login_sdata)
    def test_login_success(self,driver,user,pwd):
        page = LoginPage(driver)
        page.login(user,pwd)
        res = page.login_result(user)
        assert res,"登录成功"
        page.logout()

if __name__=="__main__":
    pytest.main('-s test_login.py -m success')
