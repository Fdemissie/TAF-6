import unittest
from projects.POMProjectDemo.common.base import BaseClass
from projects.POMProjectDemo.pages.userSignupPage import UserSignupPage
import time
import HtmlTestRunner

class SignupTest(BaseClass):

    def test_signupValid(self):
       driver = self.driver
       driver.get("http://kushena.com/register")

       signup = UserSignupPage(driver)
       signup.enterFirtname("XYZ")
       signup.enterLastname("ABC")
       signup.enterEmail("xyz2@test.com")
       signup.enterPhone("1231231232")
       signup.clickGenderRadioButton()
       signup.enterPassword("123456")
       signup.confrimPassword("123456")
       signup.clickSignupButton()
       message = signup.getDashboardMessage()
       self.assertEqual(message, "Dashboard")

       time.sleep(2)



if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:/Users/Fisseha Demissie/PycharmProjects/TAF-6/reports"))