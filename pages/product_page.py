from .base_page import BasePage
from .locators import ProductPageLocators



class ProductPage(BasePage):
    def add_item_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        button.click()

        BasePage.solve_quiz_and_get_code(self)

    def get_product_name(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        return product_name.text






