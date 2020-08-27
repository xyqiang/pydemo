from time import sleep
from web.base import Base


class TestChange(Base):
    def test_changetime(self):
        self.drvier.get("https://www.12306.cn/index/")
        time_element = self.drvier.execute_script("a=document.getElementById('train_date');a.removeAttribute('readonly')")
        sleep(3)
        self.drvier.execute_script("document.getElementById('train_date').value='2020-12-30'")
        sleep(3)
        print(self.drvier.execute_script("return document.getElementById('train_date').value"))
