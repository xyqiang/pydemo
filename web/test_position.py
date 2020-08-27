from selenium import webdriver
from selenium.webdriver.common.by import By


class TestSelecor():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.baidu.com")

    def test_send(self):
        self.driver.find_element(By.XPATH,'//*[@id="kw"]').send_keys("python")
        self.driver.find_element(By.CSS_SELECTOR,'#su').click()