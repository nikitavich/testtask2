from selenium.webdriver.common.by import By
from BaseApp import BasePage
from selenium import webdriver


class Locators:
    ELEMENT_LOCATOR = (By.XPATH, "//div[@class='category-cards']//div[1]//div[1]//div[2]//*[name()='svg']")
    ELEMENT_CHECK_BOX = (By.XPATH, "//*[text()='Check Box']")
    ELEMENT_HOME_DIRECTORY = (By.CSS_SELECTOR, "button[class='rct-collapse rct-collapse-btn']")
    ELEMENT_DOWNLOADS_DIRECTORY = (By.XPATH, "//li[3]//span[1]//button[1]//*[name()='svg']")
    ELEMENT_DOWNLOADS = (By.XPATH, "//*[text()='Downloads']")
    ELEMENT_WORDFILE = (By.XPATH, "//*[text()='Word File.doc']")
    ELEMENT_MESSAGE = (By.CSS_SELECTOR, ".text-success")


class Downloads(BasePage):
    def click_on_the_elements(self):
        element_locator = self.find_element(Locators.ELEMENT_LOCATOR)
        element_locator.click()
        return element_locator

    def click_on_the_checkbox(self):
        check_box = self.find_element(Locators.ELEMENT_CHECK_BOX)
        check_box.click()

    def click_on_the_home_directory(self):
        check_box = self.find_element(Locators.ELEMENT_HOME_DIRECTORY)
        check_box.click()
        check_box.is_displayed()
        return check_box

    def click_on_the_downloads_directory(self):
        check_box = self.find_element(Locators.ELEMENT_DOWNLOADS_DIRECTORY)
        check_box.click()
        check_box.is_displayed()
        return check_box

    def click_on_the_downloads(self):
        check_box = self.find_element(Locators.ELEMENT_DOWNLOADS)
        check_box.click()
        check_box.is_displayed()
        return check_box

    def click_on_the_wordfile(self):
        check_box = self.find_element(Locators.ELEMENT_WORDFILE)
        check_box.click()
        check_box.is_displayed()
        return check_box

    def check_message(self):
        message = self.find_element(Locators.ELEMENT_MESSAGE).is_displayed()
        return message
