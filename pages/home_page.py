import allure

from locators.home_page_locators import HomePageLocators
from pages.base_page import BasePage


class HomePage(BasePage):

    @allure.step('Закрываем панель с куками')
    def close_cookie(self):
        self.click_to_element(HomePageLocators.COOKIE_BUTTON)

    @allure.step('Кликаем на верхнюю кнопку "Заказать"')
    def click_to_order_button_top(self):
        self.click_to_element(HomePageLocators.ORDER_BUTTON_TOP)

    @allure.step('Кликаем на нижнюю кнопку "Заказать"')
    def click_to_order_button_lower(self):
        self.scroll_down(HomePageLocators.ORDER_BUTTON_LOWER)
        self.click_to_element(HomePageLocators.ORDER_BUTTON_LOWER)

    @allure.step('Кликаем на кнопку "Заказть"')
    def click_to_order_button(self, order_button):
        if order_button == HomePageLocators.ORDER_BUTTON_TOP:
            self.click_to_order_button_top()
        elif order_button == HomePageLocators.ORDER_BUTTON_LOWER:
            self.click_to_order_button_lower()

    @allure.step('Кликаем на лого "Яндекс"')
    def go_to_ya_logo(self):
        self.click_to_element(HomePageLocators.YA_LOGO_BUTTON)

    @allure.step('Проверяем что открылась страница "Дзен"')
    def check_dzen_page(self, index_page):
        self.go_to_new_window(index_page)
        self.url_change('https://dzen.ru/?yredirect=true')
        return self.get_current_url()

    @allure.step('Кликаем на лого "Самокат"')
    def go_to_scooter_logo(self):
        self.click_to_element(HomePageLocators.SCOOTER_LOGO_BUTTON)

    @allure.step('Проверяем что открылась страница "Самокат"')
    def check_home_page(self):
        return self.find_element(HomePageLocators.SCOOTER_MAIN_TEXT).text

    @allure.step('Кликаем на вопросы')
    def click_to_question(self, questions_locators):
        self.scroll_down(questions_locators)
        self.click_to_element(questions_locators)

    @allure.step('Проверяем ответы на вопросы')
    def check_to_answer(self, answers_locators):
        return self.get_text(answers_locators).text

