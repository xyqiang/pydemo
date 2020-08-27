import os
from selenium import webdriver

class Base:
    def setup(self):
        browser = os.getenv("browser")
        if browser == "firefox":
            self.drvier = webdriver.Firefox()
        elif browser == "safari":
            self.drvier = webdriver.Safari()
        else:
            self.drvier = webdriver.Chrome()
        self.drvier.implicitly_wait(5)
        self.drvier.maximize_window()

    def teardown(self):
        self.drvier.quit()