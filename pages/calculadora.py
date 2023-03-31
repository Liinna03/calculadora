from selenium.webdriver.common.by import By

from pages.base import BasePage


class ConsultarCalculadoraPage(BasePage):
    digito = 0
    txt_input = (By.XPATH, "//input[@class='DisplayText']")
    btn_numeros = (By.XPATH, "//button[.='7']")
    btn_division = (By.XPATH, "//button[.='/']")
    btn_igual = (By.XPATH, "//button[@name='equal']")

    def click_digito(self, digito):
        element_present = self.is_element_present(*ConsultarCalculadoraPage.btn_division)
        element = self.driver.find_element(By.XPATH, "//button[.= " + digito + "]")
        element.click()

    def click_btn_dividir(self):
        self.click_element(*ConsultarCalculadoraPage.btn_division)

    def click_btn_igual(self):
        self.click_element(*ConsultarCalculadoraPage.btn_igual)

    def get_resultado(self):
        return True if self.get_value(*ConsultarCalculadoraPage.txt_input) != 0 else False
