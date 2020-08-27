from web.base import Base


class TestFrame(Base):
    def test_frame(self):
        self.drvier.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
        # self.drvier.switch_to_frame("iframeResult")
        self.drvier.switch_to.frame("iframeResult")
        print(self.drvier.find_element_by_id("draggable").text)

        # self.drvier.switch_to.default_content()
        self.drvier.switch_to.parent_frame()
        print(self.drvier.find_element_by_id("submitBTN").text)