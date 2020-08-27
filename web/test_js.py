from time import sleep

import pytest

from web.base import Base


class TestJs(Base):
    @pytest.mark.skip
    def test_js(self):
        self.drvier.get("https://www.baidu.com")
        self.drvier.find_element_by_id("kw").send_keys("python")
        element = self.drvier.execute_script("return document.getElementById('su')")
        element.click()
        self.drvier.execute_script("document.documentElement.scrollTop=10000")
        sleep(3)
        self.drvier.find_element_by_xpath('//*[@id="page"]/div/a[10]').click()
        sleep(3)

        for code in [
            "return document.title","return JSON.stringify(performance.timing)"
        ]:
            print(self.drvier.execute_script(code))

        print(self.drvier.execute_script("return document.title;return JSON.stringify(performance.timing)"))

    def test_changetime(self):
        self.drvier.get("https://www.12306.cn/index/")
        time_element = self.drvier.execute_script("a=document.getElementById('train_date');a.removeAttribute('readonly')")
        sleep(3)
        self.drvier.execute_script("document.getElementById('train_date').value='2020-12-30'")
        sleep(3)
        print(self.drvier.execute_script("return document.getElementById('train_date').value"))



