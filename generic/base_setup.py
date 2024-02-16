from pyjavaproperties import Properties
import pytest
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import Remote

class BaseSetup:
    @pytest.fixture(autouse=True)
    def precondition(self):
        pptobj = Properties()
        pptobj.load(open('config.properties'))
        gridurl = pptobj['GRIDURL'].lower()
        print("Grid URL", gridurl)
        self.xl_path = pptobj['XL_PATH']
        print("XL Path", self.xl_path)

        usegrid = pptobj['USERGRID'].lower()
        print("Use Grid", usegrid)
        browser = pptobj['BROWSER']
        print("Browser", browser)
        appurl = pptobj['APPURL']
        print("AppURL", appurl)
        ito = pptobj['IMPLICIT_TIME_OUT']
        print("ITO", ito)
        eto = pptobj['EXPLICIT_TIME_OUT']
        print("ETO", eto)
        if usegrid == 'yes':
            print("Executing in remote system")
            if browser == 'chrome':
                print("Open chrome browser")
                self.driver = webdriver.Remote(command_executor=gridurl, options=webdriver.ChromeOptions())

            elif browser == 'firefox':
                print("Open firefox browser")
                self.driver = webdriver.Remote(command_executor=gridurl, options=webdriver.FirefoxOptions())

            else:
                print("Open edge browser")
                self.driver = webdriver.Remote(command_executor=gridurl, options=webdriver.EdgeOptions())

        else:
            print("Executing in local system")
            if browser == 'chrome':
                print("Open chrome browser")
                self.driver = webdriver.Chrome()

            elif browser == 'firefox':
                print("Open firefox browser")
                self.driver = webdriver.Firefox()

            else:
                print("Open edge browser")
                self.driver = webdriver.Edge()
        print("Enter the URL", appurl)
        self.driver.get(appurl)
        print("Maximize the browser")
        self.driver.maximize_window()
        print("Set ito", ito, 'seconds')
        self.driver.implicitly_wait(ito)
        print("Set eto", eto, 'seconds')
        self.wait = WebDriverWait(self.driver, eto)

    @pytest.fixture(autouse=True)
    def postcondition(self):
        yield
        print("Close the browser")
        self.driver.quit()

