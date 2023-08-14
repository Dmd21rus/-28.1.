Запуск тестов:
python3 -m pytest -v --driver Chrome --driver-path ~/chrome tests/*
или
pytest -v --driver Chrome --driver-path ~/chrome tests/*
Пример:
pytest -v --driver Chrome --driver-path ../chromedriver.exe tests/ tests/test_rtc_signin_auth.py.py
или
pytest -v -k test --driver Chrome --driver-path ../chromedriver.exe tests/


Создать в директории проекта файл .env, в него записать:
VALID_EMAIL = 'email'
VALID_LOGIN = 'account'
VALID_PASSWORD = 'password'


constants.py – содержит константы использованные в автотестах.
pages/base.py – содержит основные действия над веб-страницей: вход по заданному URL, перемещение назад-вперед, вверх-вниз и т.д.
pages/elements.py – содержит класс-помощник для работы с веб-элементами на веб-страницах.
tests/test_rtc_form_elements.py – содержит тест-кейсы: авторизация по паролю, авторизация по коду, восстановление пароля и регистрация.
tests/test_rtc_register_email.py – содержит тест-кейсы  регистрации поля ввода email – проверки валидации.
tests/test_rtc_register_name.py – содержит тест-кейсы  регистрации полей ввода имени и фамилии – проверки валидации.
tests/test_rtc_register_passw.py – содержит тест-кейсы  полей ввода пароля – проверки валидации.
tests/test_rtc_register_phone.py – содержит тест-кейсы  поля ввода номера телефона – проверки валидации.
tests/test_rtc_signin_auth.py – содержит тест-кейсы для  авторизации по паролю с использованием email или логина.



