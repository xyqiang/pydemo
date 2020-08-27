from selenium.webdriver.common.by import By
from web.weworkmain.page.addmember import AddMember
from web.weworkmain.page.basepage import BasePage

class Main(BasePage):
    _base_url = "https://work.weixin.qq.com/wework_admin/frame#index"
    def goto_add_member(self):
        # self._driver.find_element(By.CSS_SELECTOR,'.index_service_cnt_itemWrap:nth-child(1)').click()
        self.find(By.ID,'menu_contacts').click()
        self.wait_for_click((By.CSS_SELECTOR,'.js_has_member>div:nth-child(1)>a:nth-child(2)'))
        self.find(By.CSS_SELECTOR,'.js_has_member>div:nth-child(1)>a:nth-child(2)').click()
        return AddMember(self._driver)