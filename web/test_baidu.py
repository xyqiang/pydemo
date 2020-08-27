import shelve
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class TestBaidu:
    def setup(self):
        options = Options()
        options.debugger_address = "127.0.0.1:9999"
        # self.driver = webdriver.Chrome(options=options)
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)

    def teardown(self):
        self.driver.quit()

    def test_baidu(self):
        # self.driver.get("https://www.baidu.com")
        # self.driver.find_element_by_id("kw").send_keys("python")
        # self.driver.find_element_by_id("su").click()
        # self.driver.find_element_by_id("menu_contacts").click()
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        db = shelve.open("cookies")
        # db["cookie"] = self.driver.get_cookies()
        cookies = db["cookie"]
        for cookie in cookies:
            if "expiry" in cookie.keys():
                cookie.pop("expiry")
            self.driver.add_cookie(cookie)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        # print(self.driver.get_cookies())
        sleep(5)
        db.close()