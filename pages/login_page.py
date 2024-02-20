from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class LoginPage:
    __username = (By.ID, "username")
    __password = (By.NAME, "pwd")
    __loginbutton = (By.ID, "loginButton")
    __errmsg = (By.XPATH, "//span[contains(text(),'invalid')]")

    def __init__(self, driver):
        self.__driver = driver

    def set_username(self, un):
        self.__driver.find_element(*self.__username).send_keys(un)

    def set_password(self, pw):
        self.__driver.find_element(*self.__password).send_keys(pw)

    def click_loginButton(self):
        self.__driver.find_element(*self.__loginbutton).click()

    def verify_err_msg_is_displayed(self, wait: WebDriverWait):
        try:
            wait.until(expected_conditions.visibility_of_element_located(self.__errmsg))
            print("Error message is displayed")
            return True
        except:
            print("Error message is not displayed")
            return False

    def verify_login_page_is_displayed(self, wait: WebDriverWait):
        try:
            wait.until(expected_conditions.visibility_of_element_located(self.__loginbutton))
            print("Login page is displayed")
            return True
        except:
            print("Login page is not displayed")
            return False

