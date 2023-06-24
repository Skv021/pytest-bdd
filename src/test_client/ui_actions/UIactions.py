class UIactions:


    def __init__(self, driver):
        self.driver = driver

    def locate_element(self, locator):
        return self.driver.find_element(*locator)

    def enter_text(self, element, data):
        e = self.locate_element(element)
        e.send_keys(data)

    def click_element(self, element):
        e = self.locate_element(element)
        e.click()
