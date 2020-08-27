from time import sleep
from selenium.webdriver import ActionChains
from web.base import Base


class TestAlert(Base):
    def test_alert(self):
        self.drvier.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
        self.drvier.switch_to_frame("iframeResult")
        drag = self.drvier.find_element_by_id("draggable")
        drop = self.drvier.find_element_by_id("droppable")

        action = ActionChains(self.drvier)
        action.drag_and_drop(drag,drop).perform()
        sleep(3)
        self.drvier.switch_to.alert.accept()
        self.drvier.switch_to.default_content()
        self.drvier.find_element_by_id("submitBTN").click()
        sleep(3)

