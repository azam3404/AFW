from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class EnterTimeTrackPage:
    __logout = (By.ID, "logoutLink")

    def __init__(self, driver):
        self.__driver = driver

    def verify_home_page_is_displayed(self, wait: WebDriverWait):
        try:
            wait.until(expected_conditions.visibility_of_element_located(self.__logout))
            print("Home page is displayed")
            return True
        except:
            print("Home page is not displayed")
            return False

    def click_logout_link(self):
        self.__driver.find_element(*self.__logout).click()