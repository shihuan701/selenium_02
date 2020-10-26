from selenium.webdriver.common.by import By
from myselenium.page.add_member_page import AddMember
from myselenium.page.base_page import BasePage


class MainPage(BasePage):
    _base_url = 'https://work.weixin.qq.com/wework_admin/frame#index'

    def goto_addmember_index(self):
        self.find(By.CSS_SELECTOR,'.index_service_cnt_itemWrap:nth-child(1)').click()
        return AddMember

    def goto_addmember_nav(self):
        self.find(By.CSS_SELECTOR, '#menu_contacts').click()

        '''
        # 方法1:显式等待按钮可点击后再点击
        locator = (By.CSS_SELECTOR, '.js_has_member>div:nth-child(1)>a:nth-child(2)')
        # self.find(By.CSS_SELECTOR, '.js_has_member>div:nth-child(1)>a:nth-child(2)').click()
        ele = self.wait_for_loading(timeout=10, locator=locator)
        ele.click()
        '''

        # 方法2，再下一个元素出现之前持续点击添加成员按钮
        def add_member_condition(_driver):
            isExit = self.isElementExist(By.ID,'username')
            if isExit != True:
                self.find(By.CSS_SELECTOR, '.js_has_member>div:nth-child(1)>a:nth-child(2)').click()
                return False
            else:
                return True
        self.wait_for_condition(timeout=10, condition=add_member_condition)
        return AddMember
