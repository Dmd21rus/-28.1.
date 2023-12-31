from constants import RTC
from pages.rtc_register_page import RegisterMainPage
from pages.rtc_recovery_form_page import RecoveryMainPage
from pages.rtc_auth_code_page import GetCodeMainPage
from pages.rtc_signin_page import SigninMainPage
import pytest


@pytest.mark.parametrize("product",
 [RTC.URL_ELK_WEB, RTC.URL_START_WEB, RTC.URL_SMARTHOME_WEB, RTC.URL_KEY_WEB])
def test_register_form_elements(web_browser, product):

    page = RegisterMainPage(web_browser, product)
    if product == RTC.URL_KEY_WEB:
        page.key_form_enter_button.click()

    page.by_pass_button.click()
    page.register_link.click()

    assert page.title_register_name.is_presented()
    assert page.title_register_name.get_text() == RTC.REGISTRATION_TEXT
    assert page.personal_data.is_presented()
    assert page.register_button.get_text() == RTC.REGISTER_BUTTON_TEXT


@pytest.mark.parametrize("product", [RTC.URL_ELK_WEB, RTC.URL_ONLIME_WEB,
  RTC.URL_START_WEB, RTC.URL_SMARTHOME_WEB, RTC.URL_KEY_WEB])
def test_recovery_form_elements(web_browser, product):

    page = RecoveryMainPage(web_browser, product)
    if product == RTC.URL_KEY_WEB:
        page.key_form_enter_button.click()

    page.by_pass_button.click()
    page.forgot_password.click()

    assert page.title_top.is_presented()
    assert page.title_top.get_text() == RTC.RECOVERY_INSCRIPTION_TEXT
    assert page.captcha_img.is_presented()
    assert page.captcha_symbols_input_field.get_text() == \
           RTC.RECOVERY_CAPTCHA_TEXT



@pytest.mark.parametrize("product", [RTC.URL_ELK_WEB, RTC.URL_ONLIME_WEB,
  RTC.URL_START_WEB, RTC.URL_SMARTHOME_WEB, RTC.URL_KEY_WEB])
def test_auth_code_form_elements(web_browser, product):

    page = GetCodeMainPage(web_browser, product)
    if product == RTC.URL_KEY_WEB:
        page.key_form_enter_button.click()

    assert page.title_top.is_presented()
    assert page.title_top.get_text() == RTC.AUTH_BY_CODE_TEXT
    assert page.get_code_button.get_text() == RTC.AUTH_GET_CODE
    assert page.enter_by_pass.is_presented()


@pytest.mark.parametrize("product", [RTC.URL_ELK_WEB, RTC.URL_ONLIME_WEB,
  RTC.URL_START_WEB, RTC.URL_SMARTHOME_WEB, RTC.URL_KEY_WEB])
def test_auth_pass_form_elements(web_browser, product):

    page = SigninMainPage(web_browser, product)
    if product == RTC.URL_KEY_WEB:
        page.key_form_enter_button.click()

    page.by_pass_button.click()

    assert page.title_top.is_presented()
    assert page.title_top.get_text() == RTC.AUTH_BY_PASS_TEXT
    assert page.enter_button.get_text() == RTC.ENTER_TEXT
    assert page.enter_by_temp_code_button.is_presented()