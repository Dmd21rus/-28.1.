import os
from dotenv import load_dotenv

load_dotenv()

class RTC():

    URL_ELK_WEB = 'https://lk.rt.ru/'
    URL_ONLIME_WEB = 'https://my.rt.ru/'
    URL_START_WEB = 'https://start.rt.ru/'
    URL_SMARTHOME_WEB = 'https://lk.smarthome.rt.ru/'
    URL_KEY_WEB = 'https://key.rt.ru/'

    VALID_EMAIL = os.getenv('VALID_EMAIL')
    VALID_LOGIN = os.getenv('VALID_LOGIN')
    VALID_PASSWORD = os.getenv('VALID_PASSWORD')

    VALID_PASSWORD_8 = "_=d;-A#b"
    VALID_PASSWORD_20 = "$b_.A|S!-=/-a+,A`S|?"

    INVALID_EMAIL = '3254.doee@154456.com'
    INVALID_LOGIN = 'erwytg0'
    INVALID_PASSWORD = 'bsyuhr6u7d'

    COOKIES_FILE = 'rtc_cookies.txt'

    REGISTRATION_TEXT = "Регистрация"
    REGISTER_BUTTON_TEXT = "Зарегистрироваться"
    RECOVERY_INSCRIPTION_TEXT = "Восстановление пароля"
    RECOVERY_CAPTCHA_TEXT = "Символы"
    AUTH_BY_CODE_TEXT = "Авторизация по коду"
    AUTH_GET_CODE = "Получить код"
    AUTH_BY_PASS_TEXT = "Авторизация"
    ENTER_TEXT = "Войти"
    ERROR_NOTIFICATION_TEXT = "Неверный логин или пароль"
    PERSONAL_CABINET_TEXT = "Личный кабинет"
