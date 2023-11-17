from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        self.driver.get(url)

    def find_element(self, locator):
        return WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(locator))

    def url_change(self, expected_url):
        return WebDriverWait(self.driver, 10).until(EC.url_to_be(expected_url))

    def click_to_element(self, locator):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))
        self.driver.find_element(*locator).click()

    def set_text_to_element(self, locator, text):
        self.driver.find_element(*locator).send_keys(text)

    def get_text(self, locator):
        return WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(locator))

    def scroll_down(self, locator):
        element = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def go_to_new_window(self, index_page):
        self.driver.switch_to.window(self.driver.window_handles[index_page])

    def get_current_url(self):
        return self.driver.current_url


