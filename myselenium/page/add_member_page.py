from selenium.webdriver.common.by import By
from myselenium.page.base_page import BasePage


class AddMember(BasePage):


    def add_member(self,username,acctid,phone):
        self.find(By.ID,'username').send_keys(username)
        self.find(By.ID, 'memberAdd_acctid').send_keys(acctid)
        self.find(By.ID, 'memberAdd_phone').send_keys(phone)
        self.find(By.CSS_SELECTOR, '.js_btn_save').click()
        checkbox_element = (By.CSS_SELECTOR,'.ww_checkbox')
        self.wait_for_loading(timeout=3,locator=checkbox_element)
        return True



    def get_member(self,username):
        # 这个方法用于校验断言
        namelist = []
        while True:
            username_element = self.finds(By.CSS_SELECTOR, '.member_colRight_memberTable_td:nth-child(2)')
            usernamelist=[]
            for i in username_element:
                usernamelist.append(i.get_attribute('title'))
            namelist = namelist + usernamelist
            print('namelist:', namelist)
            if username in usernamelist:
                break
            # 判断是否存在分页
            flag = self.isElementExist(By.CSS_SELECTOR, '.ww_pageNav_info_text')
            if flag:
                result: str = self.find(By.CSS_SELECTOR, ".ww_pageNav_info_text").text
                num,total = result.split('/',1)
                if int(num) == int(total):
                    return False
                else:
                    self.find(By.CSS_SELECTOR, '.ww_commonImg_PageNavArrowRightNormal').click()
            else:
                break
        return namelist






