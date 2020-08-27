from selenium.webdriver.common.by import By
from web.weworkmain.page.basepage import BasePage

class AddMember(BasePage):

    def add_member(self):
        self.find(By.ID,'username').send_keys("ruichen")
        self.find(By.ID, 'memberAdd_acctid').send_keys("ruichen")
        self.find(By.ID, 'memberAdd_phone').send_keys("18500000000")
        self.find(By.CSS_SELECTOR,'.js_btn_save').click()

    def update_page(self):
        content = self.find(By.CSS_SELECTOR,'.ww_pageNav_info_text').text
        return [int(x) for x in content.split("/")]

    def get_member(self,value):
        self.wait_for_click((By.CSS_SELECTOR,'.ww_checkbox'))
        cur_page,total_page = self.update_page()
        while True:
            elements = self.finds(By.CSS_SELECTOR,'.member_colRight_memberTable_td:nth-child(2)')
            for element in elements:
                if value == element.get_attribute("title"):
                    return True

            content:str = self.find(By.CSS_SELECTOR,'.ww_pageNav_info_text').text
            cur_page = self.update_page()[0]
            if cur_page == total_page:
                return False
            self.find(By.CSS_SELECTOR,'.js_next_page').click()