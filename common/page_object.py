# -*- coding: utf-8 -*-
# @Time    : 2019/6/1 0001 9:36:29
# @Author  : zll
# @File    : page_object.py
import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from common.page_log import log1
from common.page_read import ReadConfig


class ObjectPage(object):

    browser = ReadConfig().getValue(section='browserType', name='browserName')

    chrome_driver_path = ReadConfig().getValue(section='located', name='chromedriverpath')
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('disable-infobars')
    chrome_options.add_argument("headless")
    chrome_options.add_argument('profile.managed_default_content_settings.images')
    chrome_options.add_argument('lang=zh_CN.UTF-8')
    chrome_options.add_argument('user-agent="Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36"')

    firefox_driver_path = ReadConfig().getValue(section='located', name='firefoxdriverpath')
    firefox_log_path = ReadConfig().getValue(section='located', name='firefox_log')
    firefox_options = webdriver.FirefoxOptions()
    firefox_options.add_argument('--log error')
    firefox_options.add_argument('--headless')
    firefox_options.add_argument('--disable-gpu')  # 禁用GPU加速

    def __init__(self):
        driver = self.getBrowsers()
        try:
            log1.info("-------------------- test start --------------------")
            self.driver = driver
            log1.info("Load Web Driver Success")
        except Exception:
            log1.error("Load Web Driver Fail", exc_info=1)
            self.getImage("Load Web Driver Fail")

    def getBrowsers(self):
        if self.browser == "Chrome":
            self.driver = webdriver.Chrome(executable_path = self.chrome_driver_path, chrome_options = self.chrome_options)
        elif self.browser == "Firefox":
            self.driver = webdriver.Firefox(executable_path = self.firefox_driver_path, firefox_options = self.firefox_options, log_path = self.firefox_log_path)
        return self.driver

    def getUrl(self, url):
        self.driver.get(url)
        log1.info("Set Url is: "+url)

    def hideWait(self, times):
        self.driver.implicitly_wait(times)
        log1.info("Set Implicitly Wait: "+str(times))

    def maximizeWindow(self):
        self.driver.maximize_window()
        log1.info("Set Browser Max")

    def clearCookies(self):
        self.driver.delete_all_cookies()
        log1.info("Clear All Cookies")

    def refreshBrowser(self):
        self.driver.refresh()
        log1.info("Browser Refresh")

    def getCurrentUrl(self):
        url = self.driver.current_url()
        log1.info("Get Browser Url, The Url is: "+url)
        return url

    @staticmethod
    def isDisplayed(element):
        is_display = element.is_displayed()
        log1.info("Element displayed is: "+is_display)
        return is_display

    @staticmethod
    def sleepWait(times):
        time.sleep(times)
        log1.info("Set Sleep Time is: "+str(times))

    @staticmethod
    def isSelect(element):
        log1.info("Element is Select")
        return element.is_selected()

    def findElement(self, by, value):
        by_map = {'id': By.ID, 'name': By.NAME, 'class': By.CLASS_NAME, 'tag': By.TAG_NAME, 'link': By.LINK_TEXT, 'plink': By.PARTIAL_LINK_TEXT, 'css': By.CSS_SELECTOR, 'xpath': By.XPATH}
        if by in by_map.keys():
            try:
                element = WebDriverWait(self.driver, 10, ignored_exceptions=None).until(
                    EC.presence_of_element_located((by_map[by], value)))
                log1.info(by+" Query Element: "+value)
                return element
            except NoSuchElementException:
                log1.error("Not Found Element Or Timeout", exc_info=1)
                self.getImage("Not Found Element Or Timeout")
        else:
            log1.error(by+" Variable Error", exc_info=1)
            self.getImage(by+" Variable Error")
        # element = None
        # if by in ['id', 'name', 'class', 'tag', 'link', 'plink', 'css', 'xpath']:
        #     try:
        #         if by == 'id':
        #             element = WebDriverWait(self.driver, 10, ignored_exceptions=None).until(
        #                 EC.presence_of_element_located((By.ID, value)))
        #             log1.info("Id Query Element: "+value)
        #         elif by == 'name':
        #             element = WebDriverWait(self.driver, 10, ignored_exceptions=None).until(
        #                 EC.presence_of_element_located((By.NAME, value)))
        #             log1.info("Name Query Element: "+value)
        #         elif by == 'class':
        #             element = WebDriverWait(self.driver, 10, ignored_exceptions=None).until(
        #                 EC.presence_of_element_located((By.CLASS_NAME, value)))
        #             log1.info("Class Name Query Element: "+value)
        #         elif by == 'tag':
        #             element = WebDriverWait(self.driver, 10, ignored_exceptions=None).until(
        #                 EC.presence_of_element_located((By.TAG_NAME, value)))
        #             log1.info("Tag Name Query Element: "+value)
        #         elif by == 'link':
        #             element = WebDriverWait(self.driver, 10, ignored_exceptions=None).until(
        #                 EC.presence_of_element_located((By.LINK_TEXT, value)))
        #             log1.info("Link Query Element: "+value)
        #         elif by == 'plink':
        #             element = WebDriverWait(self.driver, 10, ignored_exceptions=None).until(
        #                 EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, value)))
        #             log1.info("Partial Link Query Element: "+value)
        #         elif by == 'css':
        #             element = WebDriverWait(self.driver, 10, ignored_exceptions=None).until(
        #                 EC.presence_of_element_located((By.CSS_SELECTOR, value)))
        #             log1.info("Css Query Element: "+value)
        #         elif by == 'xpath':
        #             element = WebDriverWait(self.driver, 10, ignored_exceptions=None).until(
        #                 EC.presence_of_element_located((By.XPATH, value)))
        #             log1.info("Xpath Query Element: "+value)
        #         return element
        #     except NoSuchElementException:
        #         log1.error("Not Found Element Or Timeout", exc_info=1)
        #         self.getImage("Not Found Element Or Timeout")
        #
        # else:
        #     log1.error("Variable Error", exc_info=1)
        #     self.getImage("Variable Error")

    def findElements(self, by, value):
        by_map = {'id': By.ID, 'name': By.NAME, 'class': By.CLASS_NAME, 'tag': By.TAG_NAME, 'link': By.LINK_TEXT,
                  'plink': By.PARTIAL_LINK_TEXT, 'css': By.CSS_SELECTOR, 'xpath': By.XPATH}
        if by in by_map.keys():
            try:
                elements = WebDriverWait(self.driver, 10, ignored_exceptions=None).until(
                    EC.presence_of_all_elements_located((by_map[by], value)))
                log1.info(by + " Query Element: " + value)
                return elements
            except NoSuchElementException:
                log1.error("Not Found Element Or Timeout", exc_info=1)
                self.getImage("Not Found Element Or Timeout")
        else:
            log1.error(by + " Variable Error", exc_info=1)
            self.getImage(by + " Variable Error")
        # element = None
        # if by in ['id', 'name', 'class', 'tag', 'link', 'plink', 'css', 'xpath']:
        #     try:
        #         if by == 'id':
        #             element = self.driver.find_elements_by_id(value)
        #             log1.info("Id Query Elements "+value)
        #         elif by == 'name':
        #             element = self.driver.find_elements_by_name(value)
        #             log1.info("Name Query Elements "+value)
        #         elif by == 'class':
        #             element = self.driver.find_elements_by_class_name(value)
        #             log1.info("Class Name Query Elements "+value)
        #         elif by == 'tag':
        #             element = self.driver.find_elements_by_tag_name(value)
        #             log1.info("Tag Name Query Elements "+value)
        #         elif by == 'link':
        #             element = self.driver.find_elements_by_link_text(value)
        #             log1.info("Link Query Elements "+value)
        #         elif by == 'plink':
        #             element = self.driver.find_elements_by_partial_link_text(value)
        #             log1.info("Partial Link Query Elements "+value)
        #         elif by == 'css':
        #             element = self.driver.find_elements_by_css_selector(value)
        #             log1.info("Css Query Elements "+value)
        #         elif by == 'xpath':
        #             element = self.driver.find_elements_by_xpath(value)
        #             log1.info("Xpath Query Elements "+value)
        #         log1.info("Found Element")
        #         return element
        #     except NoSuchElementException:
        #         log1.error("Not Found Element Or Timeout", exc_info=1)
        #         self.getImage("Not Found Element Or Timeout")
        # else:
        #     log1.error("Variable Error", exc_info=1)
        #     self.getImage("Variable Error")

    @staticmethod
    def sendKeys(self, element, text):
        element.clear()
        log1.info("Element Clear Text")
        try:
            element.send_keys(text)
            log1.info("Element Input Text: "+text)
        except BaseException:
            log1.error("Not Found Element Or Input Error", exc_info=1)
            self.getImage("Not Found Element Or Input Error")

    def click(self, element):
        try:
            element.click()
            log1.info("Element Click")
        except BaseException:
            if self.isDisplayed(element) is True:
                self.sleepWait(3)
                element.click()
                log1.info("Element Click")
            else:
                log1.error('Not Found Element', exc_info=1)

    def getTitle(self):
        log1.info("Get Title")
        return self.driver.title

    def actionsKeyDown(self):
        ActionChains(self.driver).key_down(Keys.CONTROL).perform()

    def actionsKeyUp(self):
        ActionChains(self.driver).key_up(Keys.CONTROL).perform()

    @staticmethod
    def select(type, element, value):
        try:
            if type == "index":
                Select(element).select_by_index(value)
                log1.info("Select Element Index")
            elif type == "value":
                Select(element).select_by_value(value)
                log1.info("Select Element Value")
            elif type == "text":
                Select(element).select_by_visible_text(value)
                log1.info("Select Element text")
            else:
                log1.error('please input type', exc_info=1)
        except BaseException:
            log1.error('Not Found Element', exc_info=1)

    @staticmethod
    def deselect(type, element, value=""):
        try:
            if type == "index" and value != "":
                Select(element).deselect_by_index(value)
                log1.info("Deselect Element Index")
            elif type == "value" and value != "":
                Select(element).deselect_by_value(value)
                log1.info("Deselect Element Value")
            elif type == "text" and value != "":
                Select(element).deselect_by_visible_text(value)
                log1.info("Deselect Element Text")
            elif type == "all" and value == "":
                Select(element).deselect_all()
                log1.info("Deselect All Element")
            else:
                log1.error('please input type', exc_info=1)
        except BaseException:
            log1.error("Not Found Select")

    @staticmethod
    def getAllSelect(element):
        try:
            log1.info("Get All Select")
            return Select(element).all_selected_options
        except BaseException:
            log1.error("Not Found All Select")

    @staticmethod
    def getAttribute(element, attribute):
        log1.info("Get Element Attribute")
        return element.get_attribute(attribute)

    @staticmethod
    def getText(element):
        log1.info("Get Element Text")
        return element.text

    def getImage(self, imageName):
        img = ReadConfig().getValue(section='located', name='image')
        try:
            self.driver.get_screenshot_as_file(img + imageName + ".png")
            log1.info("Screenshot Image")
        except BaseException:
            log1.error("Screenshot Image Fail", exc_info=1)

    def textAlert(self):
        t = str(self.driver.switch_to.alert.text)
        log1.info("Get Alert Text: "+t)
        self.acceptAlert()
        return t

    def sendKeysAlert(self, text):
        self.driver.switch_to.alert.send_keys(text)
        log1.info("Input Alert Text: "+text)
        self.acceptAlert()

    def acceptAlert(self):
        self.driver.switch_to.alert.accept()
        log1.info("Alert Accept")

    def dismissAlert(self):
        self.driver.switch_to.alert.dismiss()
        log1.info("Alert Dismiss")

    def quitBrowser(self):
        self.sleepWait(3)
        self.driver.quit()
        log1.info("Quit Browser")
        log1.info("-------------------- test end --------------------")

    def closeBrowser(self):
        self.sleepWait(3)
        self.driver.close()
        log1.info("Close Browser")
        log1.info("-------------------- test end --------------------")
