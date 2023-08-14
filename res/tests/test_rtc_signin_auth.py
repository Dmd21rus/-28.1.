import time
import pytest
from constants import RTC
from pages.rtc_signin_page import SigninMainPage


@pytest.mark.parametrize("email_login", [RTC.VALID_EMAIL, RTC.VALID_LOGIN])
@pytest.mark.parametrize("password", [RTC.VALID_PASSWORD])
@pytest.mark.parametrize("product", [RTC.URL_ELK_WEB, RTC.URL_ONLIME_WEB,
  RTC.URL_START_WEB, RTC.URL_SMARTHOME_WEB, RTC.URL_KEY_WEB])
def test_sign_in_valid(web_browser, product, email_login, password):

    page = SigninMainPage(web_browser, product)
    if product == RTC.URL_KEY_WEB:
        page.key_form_enter_button.click()

    page.by_pass_button.click()

    page.username_field = email_login
    page.password_field = password

    page.enter_button.click()

    if product == RTC.URL_KEY_WEB:
        assert page.rostelecom_slogan_key.is_presented()

        page.exit_Key_Web.click(hold_seconds=2)
    else:
        assert page.personal_cabinet.is_presented() or \
               page.personal_cabinet_onlime.is_presented() or \
               page.personal_cabinet_smarthome.is_presented()


@pytest.mark.parametrize("email_login",
  [RTC.INVALID_EMAIL, RTC.INVALID_LOGIN])
@pytest.mark.parametrize("password", [RTC.VALID_PASSWORD, RTC.INVALID_PASSWORD])
@pytest.mark.parametrize("product", [RTC.URL_ELK_WEB, RTC.URL_ONLIME_WEB,
  RTC.URL_START_WEB, RTC.URL_SMARTHOME_WEB, RTC.URL_KEY_WEB])
def test_sign_in_invalid_email(web_browser, product, email_login, password):

    page = SigninMainPage(web_browser, product)
    if product == RTC.URL_KEY_WEB:
        page.key_form_enter_button.click()

    page.by_pass_button.click()

    page.username_field = email_login
    page.password_field = password

    page.enter_button.click()

    assert page.auth_error_message.is_presented()

    if page.auth_error_message.is_presented():

        page.username_field = RTC.VALID_EMAIL
        page.password_field = RTC.VALID_PASSWORD

        page.enter_button.click()



@pytest.mark.parametrize("email_login", [RTC.VALID_EMAIL, RTC.INVALID_EMAIL,
  RTC.VALID_LOGIN, RTC.INVALID_LOGIN])
@pytest.mark.parametrize("password", [RTC.INVALID_PASSWORD])
@pytest.mark.parametrize("product", [RTC.URL_ELK_WEB, RTC.URL_ONLIME_WEB,
   RTC.URL_START_WEB, RTC.URL_SMARTHOME_WEB, RTC.URL_KEY_WEB])
def test_sign_in_invalid_pass(web_browser, product, email_login, password):

    page = SigninMainPage(web_browser, product)
    if product == RTC.URL_KEY_WEB:
        page.key_form_enter_button.click()

    page.by_pass_button.click()

    page.username_field = email_login
    page.password_field = password

    page.enter_button.click()

    assert page.auth_error_message.is_presented()

    if page.auth_error_message.is_presented():
        page.username_field = RTC.VALID_EMAIL
        page.password_field = RTC.VALID_PASSWORD

        page.enter_button.click()