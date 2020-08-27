from time import sleep
from web.base import Base


class TestImage(Base):
    def test_image(self):
        self.drvier.get("https://image.baidu.com/")
        self.drvier.find_element_by_xpath('//*[@id="sttb"]/img[1]').click()
        self.drvier.find_element_by_id("stfile").send_keys("/Users/xyq/Documents/Study/python_study/pydemo/web/test.png")
        sleep(5)