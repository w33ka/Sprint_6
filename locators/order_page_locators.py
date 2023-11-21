from selenium.webdriver.common.by import By


class OrderPageLocators:
    # локаторы на странице заказа

    NAME_FIELD = (By.XPATH, "//input[@placeholder='* Имя']")
    SURNAME_FIELD = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_FIELD = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_DIRECTORY = (By.XPATH, "//input[@placeholder='* Станция метро']")
    METRO = (By.XPATH, "//div[contains(@class, 'select-search__select')]/ul/li")
    PHONE_NUMBER_FIELD = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")

    DELIVERY_DATE = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENT_TIME = [By.XPATH, "//div[text()='* Срок аренды']"]
    RENT_TIME_LIST = [(By.XPATH, "//div[@class='Dropdown-option' and text()='сутки']"),
                      (By.XPATH, "//div[@class='Dropdown-option' and text()='двое суток']"),
                      (By.XPATH, "//div[@class='Dropdown-option' and text()='трое суток']"),
                      (By.XPATH, "//div[@class='Dropdown-option' and text()='четверо суток']"),
                      (By.XPATH, "//div[@class='Dropdown-option' and text()='пятеро суток']"),
                      (By.XPATH, "//div[@class='Dropdown-option' and text()='шестеро суток']"),
                      (By.XPATH, "//div[@class='Dropdown-option' and text()='семеро суток']")]
    COLOR_SCOOTER = [(By.ID, "black"),
                     (By.ID, "grey")]
    COMMENT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    ORDER_BUTTON = (By.XPATH, "//div[contains(@class, 'Order_Buttons')]//button[text()='Заказать']")
    ACCEPT_BUTTON = (By.XPATH, "//button[text()='Да']")
    SUCCESS_WINDOW = (By.XPATH, "//div[@class='Order_Modal__YZ-d3']")
