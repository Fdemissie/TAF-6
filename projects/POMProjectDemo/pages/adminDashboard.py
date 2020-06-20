from projects.POMProjectDemo.locators.locators import Locators

class AdminDashboard():
    def __init__(self, driver):
        self.driver = driver
        self.profile_xpath = Locators.profile_xpath
        self.signout_xpath = Locators.signout_xpath

    def clickProfileDropdownList(self):
        self.driver.find_element_by_xpath(self.profile_xpath).click()

    def clickSignoutButton(self):
        self.driver.find_element_by_link_text(self.signout_xpath).click()