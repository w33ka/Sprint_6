import allure
import pytest

from data import Urls
from data_test import Users
from locators.home_page_locators import HomePageLocators
from pages.home_page import HomePage
from pages.order_page import OrderPage


class TestOrderPage:

    @allure.title('Проверка позитивного сценария "Заказ самоката"')
    @pytest.mark.parametrize('order_button', [
        HomePageLocators.ORDER_BUTTON_TOP,
        HomePageLocators.ORDER_BUTTON_LOWER
    ])
    def test_create_order(self, driver, order_button):
        home_page = HomePage(driver)
        home_page.open(Urls.BASE_URL)
        home_page.close_cookie()
        home_page.click_to_order_button(order_button)
        order_page = OrderPage(driver)
        users = Users()
        order_page.fill_order_form(users)
        assert order_page.check_success_order(), 'Заказ не был создан'
