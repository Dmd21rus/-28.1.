import os, pickle
from constants import RTC
from pages.base import WebPage
from pages.elements import WebElement
from pages.elements import ManyWebElements


class SigninMainPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL")  or RTC.URL_ELK_WEB

        super().__init__(web_driver, url)

    by_pass_button = WebElement(id="standard_auth_btn")

    title_top = WebElement(css_selector="h1.card-container__title")

    temp_code = WebElement(id="back_to_otp_btn")

    username_field = WebElement(id="username")

    password_field = WebElement(id="password")

    show_pass_glass = \
        WebElement(css_selector="div.rt-input__action svg.rt-base-icon")

    check_box_remember_me = WebElement(css_selector='span.rt-checkbox__shape')

    forgot_password = WebElement(id="forgot_password")

    enter_button = WebElement(id="kc-login")

    enter_by_temp_code_button = WebElement(id="back_to_otp_btn")

    user_agreement = WebElement(css_selector="div.auth-policy .rt-link")

    personal_cabinet_username_link = WebElement(css_selector="h2.sc-bvFjSx")

    personal_cabinet = WebElement(xpath="//div[contains(text(),'Личный кабинет')]")

    personal_cabinet_exit_button = \
        WebElement(xpath="//span[contains(text(),'Выйти')]")

    key_form_enter_button = WebElement(css_selector="a.go_kab")

    rostelecom_slogan_key = WebElement(css_selector='div.slogan--70NR0')

    exit_Key_Web = \
        WebElement(xpath="//span[contains(text(),'Сменить учётную запись')]")

    error_notification = WebElement(xpath="//span[@id='form-error-message']")

    personal_cabinet_onlime = WebElement(xpath="//a[contains(text(),'Перейти')]")

    personal_cabinet_smarthome = WebElement(id="submit_button")

    auth_error_message = WebElement(id="form-error-message")


