from projects.POMProjectDemo.locators.locators import Locators

class AdminLoginPage():

    def __init__(self, driver):
        self.driver = driver
        self.user_textbox_id = Locators.user_textbox_id
        self.password_textbox_id = Locators.password_textbox_id
        self.login_button_xpath = Locators.login_button_xpath
        self.invalidUsername_message_xpath = Locators.invalidUsername_message_xpath

    def enterUsername(self, email):
        self.driver.find_element_by_id(self.user_textbox_id).clear()
        self.driver.find_element_by_id(self.user_textbox_id).send_keys(email)

    def enterPassword(self, password):
        self.driver.find_element_by_id(self.password_textbox_id).clear()
        self.driver.find_element_by_id(self.password_textbox_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element_by_xpath(self.login_button_xpath).click()

    def checkInvalidLogin(self):
        msg = self.driver.find_element_by_xpath(self.invalidUsername_message_xpath).text
        return msg