#coding:utf-8
import pytest
from page.houtai_page import HouTai
from page.login_page import LoginPage
from base.base import Base

class TestHoutai:
    @pytest.fixture(scope="module",autouse=True)
    def enter_houtai(self,driver,login):
        Base(driver, node="houtai").click("houtai")
        print("登录后，进入后台")

        yield
        LoginPage(driver).logout()

    def test_header(self,driver):
        res = HouTai(driver).check_text("header")
        assert res

    def test_check_aboutcd(self,driver):
        res = HouTai(driver).check_text("aboutcd")
        assert res

    def test_modulemenu(self,driver):
        res = HouTai(driver).check_text("modulemenu")
        assert res

    def test_aboutcdmenu(self,driver):
        res = HouTai(driver).check_text("aboutcdmenu")
        assert res

if __name__=="__main__":
    pytest.main("-s,test_houtai.py")

