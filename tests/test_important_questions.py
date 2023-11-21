import allure
import pytest
import data_test
from data import Urls

from locators.home_page_locators import HomePageLocators
from pages.home_page import HomePage


class TestImportantQuestions:

    @allure.title('Проверка раздела "Вопросы о важном"')
    @pytest.mark.parametrize('questions_locators, answers_locators, true_answers', [
        [HomePageLocators.QUESTION_ONE_BUTTON, HomePageLocators.ANSWER_ONE_TEXT, data_test.TRUE_ANSWER_ONE],
        [HomePageLocators.QUESTION_TWO_BUTTON, HomePageLocators.ANSWER_TWO_TEXT, data_test.TRUE_ANSWER_TWO],
        [HomePageLocators.QUESTION_THREE_BUTTON, HomePageLocators.ANSWER_THREE_TEXT, data_test.TRUE_ANSWER_THREE],
        [HomePageLocators.QUESTION_FOUR_BUTTON, HomePageLocators.ANSWER_FOUR_TEXT, data_test.TRUE_ANSWER_FOUR],
        [HomePageLocators.QUESTION_FIVE_BUTTON, HomePageLocators.ANSWER_FIVE_TEXT, data_test.TRUE_ANSWER_FIVE],
        [HomePageLocators.QUESTION_SIX_BUTTON, HomePageLocators.ANSWER_SIX_TEXT, data_test.TRUE_ANSWER_SIX],
        [HomePageLocators.QUESTION_SEVEN_BUTTON, HomePageLocators.ANSWER_SEVEN_TEXT, data_test.TRUE_ANSWER_SEVEN],
        [HomePageLocators.QUESTION_EIGHT_BUTTON, HomePageLocators.ANSWER_EIGHT_TEXT, data_test.TRUE_ANSWER_EIGHT]
    ])
    def test_answers_fqa(self, driver, questions_locators, answers_locators, true_answers):
        home_page = HomePage(driver)
        home_page.open(Urls.BASE_URL)
        home_page.close_cookie()
        home_page.click_to_question(questions_locators)
        assert home_page.check_to_answer(answers_locators) == true_answers



