from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver

    def is_element_present(self, *element, time_wait=50):
        is_present = True
        try:
            WebDriverWait(self.driver, time_wait).until(
                EC.presence_of_element_located(element))
        except Exception as e:
            print(f'El elemento {element} no fue encontrado por el siguiente error. {e}')
            is_present = False
        return is_present

    def find_element(self, *locator, time_wait=50):
        self.is_element_present(*locator, time_wait=time_wait)
        element = self.driver.find_element(*locator)
        return element

    def click_element(self, *locator):
        element = self.find_element(*locator)
        element.click()

    def get_value(self, *locator, time_wait=50):
        self.is_element_present(*locator, time_wait=time_wait)
        element = self.driver.find_element(*locator).get_attribute("value")
        return int(element)
