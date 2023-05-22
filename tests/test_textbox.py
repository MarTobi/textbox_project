from pages.textbox_page import TextBox_Page


def test_textbox(driver):
    textbox = TextBox_Page(driver, 'https://demoqa.com/text-box')
    textbox.open_site()
    textbox.fill_and_check_all_fields('Semyon Plotnikov', 'sample.a7x@gmail.com', 'Omsk', 'City')

