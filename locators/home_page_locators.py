from selenium.webdriver.common.by import By


class HomePageLocators:
    # локаторы на главной странице

    COOKIE_BUTTON = (By.ID, "rcc-confirm-button")  # кнопка закрыть куки
    YA_LOGO_BUTTON = (By.XPATH, "//*[@alt='Yandex']")  # кнопка лого яндекса
    SCOOTER_LOGO_BUTTON = (By.XPATH, "//*[@alt='Scooter']")  # кнопка лого самокат
    ORDER_BUTTON_TOP = (By.XPATH, "//*[contains(@class, 'Header_Nav')]/button[text()='Заказать']")
    # кнопка заказть вверху страницы
    ORDER_BUTTON_LOWER = (By.XPATH, "//div[contains(@class, 'Home_FinishButton')]/button[text()='Заказать']")
    # кнопка заказать внизу страницы
    SCOOTER_MAIN_TEXT = (By.XPATH, "//div[@class='Home_Header__iJKdX']")  # текст на главной странице самоката

    # локаторы вопросов

    QUESTION_ONE_BUTTON = (By.ID, "accordion__heading-0")
    QUESTION_TWO_BUTTON = (By.ID, "accordion__heading-1")
    QUESTION_THREE_BUTTON = (By.ID, "accordion__heading-2")
    QUESTION_FOUR_BUTTON = (By.ID, "accordion__heading-3")
    QUESTION_FIVE_BUTTON = (By.ID, "accordion__heading-4")
    QUESTION_SIX_BUTTON = (By.ID, "accordion__heading-5")
    QUESTION_SEVEN_BUTTON = (By.ID, "accordion__heading-6")
    QUESTION_EIGHT_BUTTON = (By.ID, "accordion__heading-7")

    # локаторы ответов

    ANSWER_ONE_TEXT = (By.ID, "accordion__panel-0")
    ANSWER_TWO_TEXT = (By.ID, "accordion__panel-1")
    ANSWER_THREE_TEXT = (By.ID, "accordion__panel-2")
    ANSWER_FOUR_TEXT = (By.ID, "accordion__panel-3")
    ANSWER_FIVE_TEXT = (By.ID, "accordion__panel-4")
    ANSWER_SIX_TEXT = (By.ID, "accordion__panel-5")
    ANSWER_SEVEN_TEXT = (By.ID, "accordion__panel-6")
    ANSWER_EIGHT_TEXT = (By.ID, "accordion__panel-7")
