from selenium.webdriver.common.by import By


class Text_Box_Locators():

    full_name = (By.XPATH, '//input[@id="userName"]')
    email = (By.XPATH, '//input[@id="userEmail"]')
    current_address = (By.XPATH, '//textarea[@id="currentAddress"]')
    permanent_address = (By.XPATH, '//textarea[@id="permanentAddress"]')
    button_submit = (By.XPATH, '//button[@id="submit"]')

    result_name = (By.XPATH, '//p[@id="name"]')
    result_email = (By.XPATH, '//p[@id="email"]')
    result_current_address = (By.XPATH, '//p[@id="currentAddress"]')
    result_permanent_address = (By.XPATH, '//p[@id="permanentAddress"]')
