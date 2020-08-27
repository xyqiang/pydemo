from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestBaidu():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window() #窗口最大化
        # self.driver.implicitly_wait(3) #隐式等待

    def teardown(self):
        self.driver.quit()

    def test_demo(self):
        self.driver.get("https://www.baidu.com")
        # sleep(1) #显示等待
        self.driver.find_element_by_id("kw").click()
        # sleep(1)
        def wait(x):
            # return self.driver.find_element_by_id("su")
            # return False
            WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable(By.ID,("su")))
        self.driver.find_element_by_id("kw").send_keys("python")
        # sleep(1)
        self.driver.find_element_by_id("su").click()

