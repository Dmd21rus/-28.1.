from constants import RTC
from pages.rtc_register_page import RegisterMainPage
import pytest
import time


@pytest.mark.parametrize("email",
 ["jt3rfoe.doe@1secmail.com", "joe4t.doe@mail.com", "JOE.DtOE@MAIL.COM",
  "joet1.doe@mail.com", "jote-doe@mail.com", "jote.doe@1-mail.com",
  "jtoe_doe@mail.com", "jote.doe@1_mail.com", "joett.doe@mail.com"])
@pytest.mark.parametrize("product",
 [RTC.URL_ELK_WEB, RTC.URL_START_WEB, RTC.URL_KEY_WEB])
def test_register_email_valid(web_browser, email, product):

    page = RegisterMainPage(web_browser, product)
    if product == RTC.URL_KEY_WEB:
        page.key_form_enter_button.click()

    page.by_pass_button.click()
    page.register_link.click()

    page.input_field_email_phone.send_keys(email)
    page.register_button.click()

    assert not page.error_email_phone.is_presented()


@pytest.mark.parametrize("email",
                         ["",
                          "email.domain.com",
                          "@domain.com",
                          "#@%^%#$@#$@#.com",
                          "joe smith <email@domain.com>",
                          "email@domain.com (joe smith)",
                          "email@domain@domain.com",
                          ".email@domain.com",
                          "email.@domain.com",
                          "email..email@domain.com",
                          "あいうえお@domain.com",
                          "email@-domain.com",
                          "email@.domain.com",
                          "email@111.222.333.44444",
                          "email@domain..com"],
                         ids=["Empty",
                              "Missing @",
                              "Missing address",
                              "Garbage",
                              "Copy/paste from address book with name",
                              "Superfluous text",
                              "Two @",
                              "Leading dot in address",
                              "Trailing dot in address",
                              "Multiple dots",
                              "Unicode chars in address",
                              "Leading dash in domain",
                              "Leading dot in domain",
                              "Invalid IP format",
                              "Multiple dots in the domain"])
@pytest.mark.parametrize("product",
 [RTC.URL_ELK_WEB, RTC.URL_START_WEB, RTC.URL_KEY_WEB])
def test_register_email_invalid(web_browser, email, product):

    page = RegisterMainPage(web_browser, product)
    if product == RTC.URL_KEY_WEB:
        page.key_form_enter_button.click()

    page.by_pass_button.click()
    page.register_link.click()

    page.input_field_email_phone.send_keys(email)
    page.register_button.click()

    assert page.error_email_phone.is_presented()

