from generic.base_setup import BaseSetup
from pages.login_page import LoginPage
import pytest
from generic.excel import Excel


class TestInvalidLogin(BaseSetup):
    @pytest.mark.run(order=2)
    def test_valid_login(self):
        un = Excel.get_data(self.xl_path, "TestInvalidLogin", 2, 1)
        pw = Excel.get_data(self.xl_path, "TestInvalidLogin", 2, 2)
        # 1.Enter Valid UN
        login_page = LoginPage(self.driver)
        login_page.set_username(un)
        # 2.Enter Valid PW
        login_page.set_password(pw)
        # 3.Click on Login Button
        login_page.click_loginButton()
        # 4.Verify that error message is dispalyed
        displayed = login_page.verify_err_msg_is_displayed(self.wait)
        assert displayed

