from time import sleep
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestForm:
    def setup(self):
        self.driver = webdriver.Chrome()

    def teardown(self):
        self.driver.quit()

    def test_form(self):
        self.driver.get("https://testerhome.com/account/sign_in")
        element = self.driver.find_element(By.XPATH,'//*[@id="user_login"]').send_keys("123")
        element1 = self.driver.find_element(By.XPATH,'//*[@id="user_password"]').send_keys("password")
        element2 = self.driver.find_element(By.XPATH,'//*[@id="user_remember_me"]').click()
        element3 = self.driver.find_element(By.XPATH,'//*[@name="commit"]').click()
        sleep(5)

if __name__ == '__main__':
    pytest.main()
