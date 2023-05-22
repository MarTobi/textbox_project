from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import datetime



class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open_site(self):
        """"Метод для открытия определенной страницы"""
        self.driver.get(self.url)


    def make_screenshots(self):
        """"Метод для создания скриншота на странице"""
        current_date = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
        name_screenshot = f'screenshot {current_date}.png'
        self.driver.save_screenshot(f"/Users/semyonplotnikov/PycharmProjects"
                                    f"/textbox_project/screenshots/{name_screenshot}")

    def check_value(self, actual_result, expected_result):
        """Проверка полученного результата с ожидаемым"""
        assert actual_result == expected_result

    # Действия, для обнаружения элементов на странице
    def element_is_visible(self, locator, timeout=30):
        return wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def element_is_present(self, locator, timeout=30):
        return wait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def element_is_clickable(self, locator, timeout=30):
        return wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def go_to_element(self, locator):
        """Метод для перемещения к элементу на странице"""
        actions = ActionChains(self.driver)
        actions.move_to_element(self.element_is_clickable(locator)).perform()
