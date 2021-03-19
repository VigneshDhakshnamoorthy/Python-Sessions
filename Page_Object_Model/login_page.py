class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.user_name_ID = "user-name"
        self.password_ID = "password"
        self.login_button_ID = "login-button"

    def enter_details (self, user_name_1, password_1):
        self.driver.find_element_by_id(self.user_name_ID).send_keys(user_name_1)
        self.driver.find_element_by_id(self.password_ID).send_keys(password_1)
        self.driver.find_element_by_id(self.login_button_ID).click()



