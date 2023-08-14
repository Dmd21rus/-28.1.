import os, pickle
from constants import RTC
from pages.base import WebPage
from pages.elements import WebElement
from pages.elements import ManyWebElements


class GetCodeMainPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL")  or RTC.URL_ELK_WEB

        super().__init__(web_driver, url)

    title_top = WebElement(css_selector="h1.card-container__title")

    get_code_button = WebElement(id="otp_get_code")

    input_field = WebElement(id="address")

    enter_by_pass = WebElement(id="standard_auth_btn")

    key_form_enter_button = WebElement(css_selector="a.go_kab")













