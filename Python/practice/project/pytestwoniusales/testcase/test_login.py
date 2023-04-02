# @Date   : 2022/9/23 15:56
# @Author : Andrew
# @Name   : test_login
import pytest
from project.pytestwoniusales.business.login import WoniusalesInterface
from project.pytestwoniusales.data.testdata import logindata


class TestLogin:

    @pytest.mark.parametrize("username, password, verifcode,exp", logindata)
    def testlogin(self, username, password, verifcode, exp):
        res = WoniusalesInterface().login(username, password, verifcode)
        assert res.text == exp
