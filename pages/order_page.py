import allure
from selenium.webdriver import Keys

from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage
import random
from data_test import Users


class OrderPage(BasePage):

    @allure.step('Заполняем Имя')
    def fill_name(self, text):
        self.set_text_to_element(OrderPageLocators.NAME_FIELD, text)

    @allure.step('Заполняем Фамилию')
    def fill_surname(self, text):
        self.set_text_to_element(OrderPageLocators.SURNAME_FIELD, text)

    @allure.step('Заполняем Адрес')
    def fill_address(self, text):
        self.set_text_to_element(OrderPageLocators.ADDRESS_FIELD, text)

    @allure.step('Заполняем Метро')
    def fill_metro(self, text):
        self.find_element(OrderPageLocators.METRO_DIRECTORY)
        self.set_text_to_element(OrderPageLocators.METRO_DIRECTORY, text)
        self.click_to_element(OrderPageLocators.METRO)

    @allure.step('Заполняем Телефон')
    def fill_phone(self, text):
        self.set_text_to_element(OrderPageLocators.PHONE_NUMBER_FIELD, text)

    @allure.step('Нажимаем кнопку Далее')
    def go_to_next(self):
        self.click_to_element(OrderPageLocators.NEXT_BUTTON)

    @allure.step('Заполняем желаемую дату доставки')
    def fill_delivery_date(self, text):
        self.set_text_to_element(OrderPageLocators.DELIVERY_DATE, text)
        self.set_text_to_element(OrderPageLocators.DELIVERY_DATE, Keys.RETURN)

    @allure.step('Выбираем срок аренды')
    def choose_rent_time(self):
        self.click_to_element(OrderPageLocators.RENT_TIME)
        self.click_to_element(random.choice(OrderPageLocators.RENT_TIME_LIST))

    @allure.step('Выбираем цвет самоката')
    def choose_color(self):
        self.click_to_element(random.choice(OrderPageLocators.COLOR_SCOOTER))

    @allure.step('Заполняем комментарий')
    def fill_comment(self, text):
        self.set_text_to_element(OrderPageLocators.COMMENT, text)

    @allure.step('Нажимаем кнопку "Заказать"')
    def go_to_order(self):
        self.click_to_element(OrderPageLocators.ORDER_BUTTON)

    @allure.step('Нажимаем кнопку "Да" подтверждая заказ')
    def accept_order(self):
        self.click_to_element(OrderPageLocators.ACCEPT_BUTTON)

    @allure.step('Проверка успешно созданного заказа')
    def check_success_order(self):
        success_order = self.find_element(OrderPageLocators.SUCCESS_WINDOW)
        return success_order is not None

    @allure.step('Заполнение полей при создании заказа')
    def fill_order_form(self, users):
        self.fill_name(users.NAME)
        self.fill_surname(users.SURNAME)
        self.fill_address(users.ADDRESS)
        self.fill_metro(users.METRO)
        self.fill_phone(users.PHONE)
        self.go_to_next()
        self.fill_delivery_date(users.DATE)
        self.choose_rent_time()
        self.choose_color()
        self.fill_comment(users.COMMENT)
        self.go_to_order()
        self.accept_order()



