from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage():
    _driver =None
    _base_url = ''

    def __init__(self,driver:WebDriver = None):
        if driver==None:
            options = Options()
            options.debugger_address='127.0.0.1:9222'
            self._driver = webdriver.Chrome(options=options)
            self._driver.implicitly_wait(3)

        else:
            self._driver = driver

        if self._base_url != '':
            self._driver.get(self._base_url)


    def find(self,by,locate):
        return self._driver.find_element(by,locate)

    def finds(self,by,locate):
        return self._driver.find_elements(by,locate)

    def wait_for_loading(self,timeout,locator):
        element:WebElement = WebDriverWait(self._driver,timeout).until(expected_conditions.element_to_be_clickable(locator))
        return element

    def wait_for_condition(self,timeout,condition):
        element:WebElement = WebDriverWait(self._driver,timeout).until(condition)
        return element

    def isElementExist(self,by,locate):
        flag = True
        try:
            self._driver.find_element(by,locate)
            return flag
        except:
            flag = False
            return flag


