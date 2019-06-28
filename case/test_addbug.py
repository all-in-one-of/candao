#coding:utf-8
import pytest
from page.addbug_page import Addbug
from page.login_page import LoginPage
from base.base import Base
from page.get_addbug_data import addbug_data
import time
bug_data=addbug_data()


class TestAddbug:
    @pytest.fixture(scope="module",autouse=True)
    def open_bugpage(self,driver,login):
        Base(driver,node="addbug").click('test')
        Base(driver,node="addbug").click('bug')
        time.sleep(2)
        yield
        LoginPage(driver).logout()

    @pytest.mark.parametrize("production,module,build,type,os,browser,severity,priority,title,body",bug_data)
    def test_addbug(self,driver,production,module,build,type,os,browser,severity,priority,title,body):
        Base(driver, node="addbug").click('addbug')
        Addbug(driver).add_bug(production,module,build,type,os,browser,severity,priority,title,body)


if __name__=="__main__":
    pytest.main('-s test_addbug.py')
