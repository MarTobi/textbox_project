from locators.textbox_locators import Text_Box_Locators
from pages.base_page import BasePage


class TextBox_Page(BasePage):
    locators = Text_Box_Locators()

    def fill_and_check_all_fields(self, full_name, email, current_address, permanent_address):
        """Метод, который заполняет все поля на странице"""
        self.element_is_clickable(self.locators.full_name).send_keys(full_name)
        print(f'\nИмя пользователя введено: "{full_name}"')
        self.element_is_clickable(self.locators.email).send_keys(email)
        print(f'Почта пользователя введена: "{email}"')
        self.element_is_clickable(self.locators.current_address).send_keys(current_address)
        print(f'Текущий адрес указан: "{current_address}"')
        self.element_is_clickable(self.locators.permanent_address).send_keys(permanent_address)
        print(f'Постоянный адрес указан: "{permanent_address}"')
        self.element_is_clickable(self.locators.button_submit).click()
        created_full_name = self.element_is_visible(self.locators.result_name).text.split(':')[1]
        created_email = self.element_is_visible(self.locators.result_email).text.split(':')[1]
        created_current_address = self.element_is_visible(self.locators.result_current_address).text.split(':')[1]
        created_permanent_address = self.element_is_visible(self.locators.result_permanent_address).text.split(':')[1]
        # self.make_screenshots()
        self.check_value(full_name, created_full_name)
        self.check_value(email, created_email)
        self.check_value(current_address, created_current_address)
        self.check_value(permanent_address, created_permanent_address)
        print(f'Полученные данные совпадают с введенной ранее информацией:'
              f' \n{created_full_name} \n{created_email} \n{created_current_address} \n{created_permanent_address}')








