import os
from constants import RTC
from pages.base import WebPage
from pages.elements import WebElement
from pages.elements import ManyWebElements


class RegisterMainPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL")  or RTC.URL_ELK_WEB

        super().__init__(web_driver, url)

    by_pass_button = WebElement(id="standard_auth_btn")

    key_form_enter_button = WebElement(css_selector="a.go_kab")

    register_link = WebElement(id="kc-register")

    title_register_name = \
        WebElement(css_selector="h1.card-container__title")

    personal_data = WebElement(xpath="//p[contains(text(),'Личные данные')]")

    register_button = WebElement(xpath='//button[@name="register"]')

    input_field_name = WebElement(xpath='//input[@name="firstName"]')

    errors_names = ManyWebElements(xpath="//span[contains(text(), "
                                         "'Необходимо заполнить поле')]")
    error_name = WebElement(xpath="//span[contains(text(), "
                                  "'Необходимо заполнить поле')]")

    input_field_lastname = WebElement(xpath='//input[@name="lastName"]')

    input_field_email_phone = WebElement(id="address")

    error_email_phone = \
        WebElement(css_selector="div.email-or-phone "
                                "span.rt-input-container__meta")

    input_field_password = WebElement(id="password")

    input_field_confirm_pass = WebElement(id="password-confirm")

    passw_err_mess = \
        WebElement(css_selector=
                   'div.new-password-container__password span.rt-input-container__meta--error')

    confirm_passw_err_mess = \
        WebElement(css_selector=
                   'div.new-password-container__confirmed-password span.rt-input-container__meta--error')









