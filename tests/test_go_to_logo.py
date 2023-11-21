import allure

from data import Urls
from pages.home_page import HomePage


class TestHomePage:

    @allure.title('Проверка перехода на страницу DZEN при клике на лого "Яндекс"')
    def test_go_to_dzen(self, driver):
        home_page = HomePage(driver)
        home_page.open(Urls.BASE_URL)
        home_page.go_to_ya_logo()
        current_url = home_page.check_dzen_page(1)
        assert current_url == 'https://dzen.ru/?yredirect=true'

    @allure.title('Проверка перехода на главную страницу при клике на лого "Самокат"')
    def test_go_to_scooter(self, driver):
        home_page = HomePage(driver)
        home_page.open(Urls.BASE_URL)
        home_page.go_to_scooter_logo()
        home_page_text = home_page.check_home_page()
        assert 'Самокат' in home_page_text and 'на пару дней' in home_page_text

