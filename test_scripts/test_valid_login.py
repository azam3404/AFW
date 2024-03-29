from generic.base_setup import BaseSetup
from pages.login_page import LoginPage
from pages.enter_time_track import EnterTimeTrackPage
import pytest
from generic.excel import Excel


class TestValidLogin(BaseSetup):
    @pytest.mark.run(order=1)
    def test_valid_login(self):
        un = Excel.get_data(self.xl_path, "TestValidLogin", 2, 1)
        pw = Excel.get_data(self.xl_path, "TestValidLogin", 2, 2)
        # 1.Enter Valid UN
        login_page = LoginPage(self.driver)
        login_page.set_username(un)
        # 2.Enter Valid PW
        login_page.set_password(pw)
        # 3.Click on Login Button
        login_page.click_loginButton()
        # 4.Verify that home page is dispalyed
        ett_page = EnterTimeTrackPage(self.driver)
        displayed = ett_page.verify_home_page_is_displayed(self.wait)
        assert displayed
        print("The End")

