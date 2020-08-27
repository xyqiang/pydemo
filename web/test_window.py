from time import sleep
from selenium import webdriver
from web.base import Base

class TestWindow(Base):

    def test_window(self):
        driver = self.drvier.get("https://www.baidu.com")
        self.drvier.find_element_by_link_text("登录").click()
        self.drvier.find_element_by_link_text("立即注册").click()
        self.drvier.switch_to_window(self.drvier.window_handles[-1])
        self.drvier.find_element_by_xpath('//*[@id="TANGRAM__PSP_4__userName"]').send_keys("x55926374")
        self.drvier.find_element_by_xpath('//*[@id="TANGRAM__PSP_4__phone"]').send_keys("1380000000 ")
        sleep(3)
        self.drvier.switch_to_window(self.drvier.window_handles[0])
        self.drvier.find_element_by_xpath('//*[@id="TANGRAM__PSP_11__footerULoginBtn"]').click()
        self.drvier.find_element_by_xpath('//*[@id="TANGRAM__PSP_11__userName"]').send_keys("x239627086")
        self.drvier.find_element_by_xpath('//*[@id="TANGRAM__PSP_11__password"]').send_keys("Zxc5425230")
        self.drvier.find_element_by_xpath('//*[@id="TANGRAM__PSP_11__submit"]').click()
        sleep(3)
