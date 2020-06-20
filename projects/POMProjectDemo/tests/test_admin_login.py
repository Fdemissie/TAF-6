from selenium import webdriver
import time
import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "...", ".."))
from projects.POMProjectDemo.pages.adminLoginPage import AdminLoginPage
from projects.POMProjectDemo.pages.adminDashboard import AdminDashboard
import HtmlTestRunner
from projects.POMProjectDemo.common.base import BaseClass

class LoginTest(BaseClass):

    def test_LoginInvalid(self):
        driver = self.driver
        driver.get("URL")

        login = AdminLoginPage(driver)
        login.enterUsername('username')
        login.enterPassword('password')
        login.clickLogin()
        message = login.checkInvalidLogin()
        self.assertEqual(message, "These credentials do not match our records.")
        time.sleep(2)

    def test_LoginValid(self):
        driver = self.driver
        driver.get("URL")

        login = AdminLoginPage(driver)
        login.enterUsername('username')
        login.enterPassword('password')
        login.clickLogin()

        adminDashboard = AdminDashboard(driver)
        adminDashboard.clickProfileDropdownList()
        driver.implicitly_wait(2)
        adminDashboard.clickSignoutButton()

        time.sleep(2)




if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:/Users/Fisseha Demissie/PycharmProjects/TAF-6/reports"))

