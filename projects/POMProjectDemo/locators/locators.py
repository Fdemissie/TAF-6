class Locators():
    #login page object
    user_textbox_id = "email"
    password_textbox_id = "password"
    login_button_xpath = "//*[@id=\"signup\"]/div[3]/button"
    invalidUsername_message_xpath= "//form[@id='signup']//p[@class='help-block text-danger'][contains(text(),'These credentials do not match our records.')]"



    #admin dashboard objects
    profile_xpath = "/html/body/div[1]/div[5]/nav/div/div[2]/ul[2]/li/a"
    signout_xpath = " Sign out"


    signup_firstname_xpath = "//div[@id='second_step']//div[1]//input[1]"
    signup_lastname_xpath = "//div//div//div//div//div[2]//input[1]"
    signup_email_xpath = "//div[3]//input[1]"
    signup_phone_number_id = "phone_number"
    signup_gender_male_radio_xpath = "//label[contains(text(),'Male')]"
    signup_gender_female_radio_xpath = "//label[contains(text(),'Female')]"
    signup_password_xpath = "//div[6]//input[1]"
    signup_password_confirm_xpath = "//div[7]//input[1]"
    signup_button_xpath = "//button[contains(text(),'CADASTRAR')]"

    user_dashboard_text_linkText = "Dashboard"
