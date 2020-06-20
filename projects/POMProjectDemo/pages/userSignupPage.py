from projects.POMProjectDemo.locators.locators import Locators

class UserSignupPage():
    def __init__(self, driver):
        self.driver = driver
        self.signup_firstname_xpath = Locators.signup_firstname_xpath
        self.signup_lastname_xpath = Locators.signup_lastname_xpath
        self.signup_email_xpath = Locators.signup_email_xpath
        self.signup_phone_number_id = Locators.signup_phone_number_id
        self.signup_gender_male_radio_xpath = Locators.signup_gender_male_radio_xpath
        self.signup_gender_female_radio_xpath = Locators.signup_gender_male_radio_xpath
        self.signup_password_xpath = Locators.signup_password_xpath
        self.signup_password_confirm_xpath = Locators.signup_password_confirm_xpath
        self.signup_button_xpath = Locators.signup_button_xpath
        self.user_dashboard_text = Locators.user_dashboard_text_linkText


    def enterFirtname(self, firstname):
        self.driver.find_element_by_xpath(self.signup_firstname_xpath).clear()
        self.driver.find_element_by_xpath(self.signup_firstname_xpath).send_keys(firstname)

    def enterLastname(self, lastname):
        self.driver.find_element_by_xpath(self.signup_lastname_xpath).clear()
        self.driver.find_element_by_xpath(self.signup_lastname_xpath).send_keys(lastname)

    def enterEmail(self, email):
        self.driver.find_element_by_xpath(self.signup_email_xpath).clear()
        self.driver.find_element_by_xpath(self.signup_email_xpath).send_keys(email)

    def enterPhone(self, phone):
        self.driver.find_element_by_id(self.signup_phone_number_id).clear()
        self.driver.find_element_by_id(self.signup_phone_number_id).send_keys(phone)

    def clickGenderRadioButton(self):
        self.driver.find_element_by_xpath(self.signup_gender_male_radio_xpath).click()

    def enterPassword(self, phone):
        self.driver.find_element_by_xpath(self.signup_password_xpath).clear()
        self.driver.find_element_by_xpath(self.signup_password_xpath).send_keys(phone)

    def confrimPassword(self, phone):
        self.driver.find_element_by_xpath(self.signup_password_confirm_xpath).clear()
        self.driver.find_element_by_xpath(self.signup_password_confirm_xpath).send_keys(phone)

    def clickSignupButton(self):
        self.driver.find_element_by_xpath(self.signup_button_xpath).click()

    def getDashboardMessage(self):
        msg = self.driver.find_element_by_link_text(self.user_dashboard_text).text
        return msg


