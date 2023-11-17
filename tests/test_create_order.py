import allure
import pytest

import data_test
from locators.home_page_locators import HomePageLocators
from pages.home_page import HomePage
from pages.order_page import OrderPage


class TestOrderPage:

    @allure.title('Проверка позитивного сценария "Заказ самоката"')
    @pytest.mark.parametrize(('order_button', 'name', 'surname', 'address', 'metro', 'phone', 'date', 'comment'), [
        (HomePageLocators.ORDER_BUTTON_TOP, data_test.NAME, data_test.SURNAME, data_test.ADDRESS, data_test.METRO,
         data_test.PHONE, data_test.DATE, data_test.COMMENT),
        (HomePageLocators.ORDER_BUTTON_LOWER, data_test.NAME, data_test.SURNAME, data_test.ADDRESS, data_test.METRO,
         data_test.PHONE, data_test.DATE, data_test.COMMENT)
    ])
    def test_create_order(self, driver, order_button, name, surname, address, metro, phone, date, comment):
        home_page = HomePage(driver)
        home_page.open('https://qa-scooter.praktikum-services.ru/')
        home_page.close_cookie()
        home_page.click_to_order_button(order_button)
        order_page = OrderPage(driver)
        order_page.fill_name(name)
        order_page.fill_surname(surname)
        order_page.fill_address(address)
        order_page.fill_metro(metro)
        order_page.fill_phone(phone)
        order_page.go_to_next()
        order_page.fill_delivery_date(date)
        order_page.choose_rent_time()
        order_page.choose_color()
        order_page.fill_comment(comment)
        order_page.go_to_order()
        order_page.accept_order()
        assert order_page.check_success_order(), 'Заказ не был создан'
