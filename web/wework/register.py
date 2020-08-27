from selenium.webdriver.remote.webdriver import WebDriver

class Register:
    def __init__(self,driver: WebDriver):
        self._driver = driver

    def register(self):
        # send content
        # click element
        self._driver.find_element_by_id('corp_name').send_keys("corp_name")
        self._driver.find_element_by_id('manager_name').send_keys("manager_name")
        return True
