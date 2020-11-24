from .pages.login_page import LoginPage
from .pages.main_page import MainPage
from .pages.product_page import ProductPage
import pytest
import random
import string
import time
from selenium.common.exceptions import NoAlertPresentException
# pytest -v --tb=line --language=en test_product_page.py
# pytest -v --tb=line test_product_page.py

#PRODUCT_CODERS_AT_WORK = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"

def test_guest_can_add_product_to_basket(browser):
    #main_page = MainPage(browser, PRODUCT_CODERS_AT_WORK + "?promo=newYear2019")
    main_page = MainPage(browser,link)
    main_page.open()
    product_page = ProductPage(browser, browser.current_url)
    product_page.add_item_to_basket()



def solve_quiz_and_get_code(self):
    alert = self.browser.switch_to.alert
    x = alert.text.split(" ")[2]
    answer = str(math.log(abs((12 * math.sin(float(x))))))
    alert.send_keys(answer)
    alert.accept()
    try:
        alert = self.browser.switch_to.alert
        alert_text = alert.text
        print(f"Your code: {alert_text}")
        alert.accept()
    except NoAlertPresentException:
        print("No second alert presented")
