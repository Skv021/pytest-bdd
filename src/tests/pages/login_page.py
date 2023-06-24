from selenium.webdriver.common.by import By
#from src.test_client.ui_actions.UIactions import UIactions
from src.test_client.ui_actions.UIactions import UIactions

class Loginpage(UIactions):
    user_name = By.NAME, "userName"
    password = By.NAME, "password"
    submit_button = By.NAME, "submit"

    def __init__(self, driver):
        self.driver=driver
        super().__init__(driver)

    def enter_username(self):
        self.enter_text(self.user_name,'xyz')

    def enter_password(self):
        self.enter_text(self.password,"abc")

    def click_submit(self):
        self.click_element(self.submit_button)
