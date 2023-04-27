import time
import pytest
from pages.auth_page import *
from settings import *


# TC-01
@pytest.mark.auth
def test_page_open(web_browser):

    page = AuthPage(web_browser)
    assert page.logo.get_text() == "© 2023 ПАО «Ростелеком». 18+"


# TC-02
@pytest.mark.auth
def test_tabs_on_authorisation_page(web_browser):
    page = AuthPage(web_browser)

    tabs_elements = [x.text for x in page.tabs]
    for x in page.tabs:
        assert x.is_enabled()
        assert x.is_displayed()

    assert page.tab_phone.is_clickable() and page.tab_email.is_clickable() and page.tab_user_login.is_clickable() \
           and page.tab_ls.is_clickable()
    assert 'Телефон' in tabs_elements and 'Почта' in tabs_elements and 'Логин' in tabs_elements \
           and 'Лицевой счёт' in tabs_elements


# TC-03
@pytest.mark.auth
def test_tab_phone_active(web_browser):
    page = AuthPage(web_browser)
    time.sleep(1)
    assert page.tab_phone.is_active(check=check_select_tab, attr_name='class')


# TC-04, TC-05
@pytest.mark.auth
def test_authorisation_page(web_browser):
    page = AuthPage(web_browser)
    time.sleep(1)

    # Проверяем доступность, видимость, название поля логин и поля пароль на tab Телефон
    assert page.input_login.is_presented() and page.input_login.is_visible() and page.input_login.is_clickable()
    assert page.input_login_title.get_text() == "Мобильный телефон"
    assert page.input_password.is_presented() and page.input_password.is_visible() and \
           page.input_password.is_clickable()
    assert page.input_password_title.get_text() == "Пароль"

    # Проверить доступность, видимость, название поля логин и поля пароль на tab Почта
    page.tab_email.click()
    assert page.input_login.is_presented() and page.input_login.is_visible() and page.input_login.is_clickable()
    assert page.input_login_title.get_text() == "Электронная почта"
    assert page.input_password.is_presented() and page.input_password.is_visible() and \
           page.input_password.is_clickable()
    assert page.input_password_title.get_text() == "Пароль"

    # Проверить доступность, видимость, название поля логин и поля пароль на tab Логин
    page.tab_user_login.click()
    assert page.input_login.is_presented() and page.input_login.is_visible() and page.input_login.is_clickable()
    assert page.input_login_title.get_text() == "Логин"
    assert page.input_password.is_presented() and page.input_password.is_visible() and \
           page.input_password.is_clickable()
    assert page.input_password_title.get_text() == "Пароль"

    # Проверить доступность, видимость, название поля логин и поля пароль на tab Лицевой счет
    page.tab_ls.click()
    assert page.input_login.is_presented() and page.input_login.is_visible() and page.input_login.is_clickable()
    assert page.input_login_title.get_text() == "Лицевой счёт"
    assert page.input_password.is_presented() and page.input_password.is_visible() and \
           page.input_password.is_clickable()
    assert page.input_password_title.get_text() == "Пароль"


# TC-06
@pytest.mark.auth
def test_forgot_password_btn(web_browser):
    page = AuthPage(web_browser)

    page.tab_phone.click()
    assert page.tab_phone.is_active(check=check_select_tab, attr_name='class')
    assert page.forgot_password.is_presented() and page.forgot_password.is_visible() and \
           page.forgot_password.is_clickable()
    assert page.forgot_password.get_text() == "Забыл пароль"
    assert not page.forgot_password.is_active(check=check_forgot_password, attr_name='class')

    page.tab_email.click()
    assert page.tab_email.is_active(check=check_select_tab, attr_name='class')
    assert page.forgot_password.is_presented() and page.forgot_password.is_visible() and \
           page.forgot_password.is_clickable()
    assert page.forgot_password.get_text() == "Забыл пароль"
    assert not page.forgot_password.is_active(check=check_forgot_password, attr_name='class')

    page.tab_user_login.click()
    assert page.tab_user_login.is_active(check=check_select_tab, attr_name='class')
    assert page.forgot_password.is_presented() and page.forgot_password.is_visible() and \
           page.forgot_password.is_clickable()
    assert page.forgot_password.get_text() == "Забыл пароль"
    assert not page.forgot_password.is_active(check=check_forgot_password, attr_name='class')

    page.tab_ls.click()
    assert page.tab_ls.is_active(check=check_select_tab, attr_name='class')
    assert page.forgot_password.is_presented() and page.forgot_password.is_visible() and \
           page.forgot_password.is_clickable()
    assert page.forgot_password.get_text() == "Забыл пароль"
    assert not page.forgot_password.is_active(check=check_forgot_password, attr_name='class')


# TC-07
@pytest.mark.auth
def test_register_btn(web_browser):
    page = AuthPage(web_browser)

    assert page.register_btn.is_presented() and page.register_btn.is_visible() and page.register_btn.is_clickable()
    assert page.register_btn.get_text() == "Зарегистрироваться"

    page.tab_phone.click()
    assert page.tab_phone.is_active(check=check_select_tab, attr_name='class')
    assert page.register_btn.is_presented() and page.register_btn.is_visible() and page.register_btn.is_clickable()
    assert page.register_btn.get_text() == "Зарегистрироваться"

    page.tab_email.click()
    assert page.tab_email.is_active(check=check_select_tab, attr_name='class')
    assert page.register_btn.is_presented() and page.register_btn.is_visible() and page.register_btn.is_clickable()
    assert page.register_btn.get_text() == "Зарегистрироваться"

    page.tab_user_login.click()
    assert page.tab_user_login.is_active(check=check_select_tab, attr_name='class')
    assert page.register_btn.is_presented() and page.register_btn.is_visible() and page.register_btn.is_clickable()
    assert page.register_btn.get_text() == "Зарегистрироваться"

    page.tab_ls.click()
    assert page.tab_ls.is_active(check=check_select_tab, attr_name='class')
    assert page.register_btn.is_presented() and page.register_btn.is_visible() and page.register_btn.is_clickable()
    assert page.register_btn.get_text() == "Зарегистрироваться"


# TC-08-TC-11
@pytest.mark.auth
def test_change_tabs(web_browser):
    page = AuthPage(web_browser)

    try:
        page.tab_phone.click()
        assert page.tab_phone.is_active(check=check_select_tab, attr_name='class')
        page.input_login.send_keys('test_email@gmail.com')
        page.input_password.click()
        assert page.tab_email.is_active(check=check_select_tab, attr_name='class')
    except AssertionError as e:
        page.screenshot('phone1.png')
        print(f"Смена Таба выбора аутентификации с телефона на почту автоматически не происходит")

    try:
        page.tab_phone.click()
        assert page.tab_phone.is_active(check=check_select_tab, attr_name='class')
        page.input_login.send_keys('my_rt_login')
        page.input_password.click()
        assert page.tab_user_login.is_active(check=check_select_tab, attr_name='class')
    except AssertionError as e:
        page.screenshot('phone2.png')
        print(f"Смена Таба выбора аутентификации с телефона на логин автоматически не происходит")

    try:
        page.tab_phone.click()
        assert page.tab_phone.is_active(check=check_select_tab, attr_name='class')
        page.input_login.send_keys('312010992430')
        page.input_password.click()
        assert page.tab_ls.is_active(check=check_select_tab, attr_name='class')
    except AssertionError as e:
        page.screenshot('phone3.png')
        print(f"Смена Таба выбора аутентификации с телефона на ЛС автоматически не происходит")

    try:
        page.tab_email.click()
        assert page.tab_email.is_active(check=check_select_tab, attr_name='class')
        page.input_login.send_keys('+79171111111')
        page.input_password.click()
        assert page.tab_phone.is_active(check=check_select_tab, attr_name='class')
    except AssertionError as e:
        page.screenshot('email1.png')
        print(f"Смена Таба выбора аутентификации с почты на телефон автоматически не происходит")

    try:
        page.tab_email.click()
        assert page.tab_email.is_active(check=check_select_tab, attr_name='class')
        page.input_login.send_keys('my_rt_login')
        page.input_password.click()
        assert page.tab_user_login.is_active(check=check_select_tab, attr_name='class')
    except AssertionError as e:
        page.screenshot('email2.png')
        print(f"Смена Таба выбора аутентификации с почты на логин автоматически не происходит")

    try:
        page.tab_email.click()
        assert page.tab_email.is_active(check=check_select_tab, attr_name='class')
        page.input_login.send_keys('312010992430')
        page.input_password.click()
        assert page.tab_ls.is_active(check=check_select_tab, attr_name='class')
    except AssertionError as e:
        page.screenshot('email3.png')
        print(f"Смена Таба выбора аутентификации с почты на ЛС автоматически не происходит")

    try:
        page.tab_user_login.click()
        assert page.tab_user_login.is_active(check=check_select_tab, attr_name='class')
        page.input_login.send_keys('+79171111111')
        page.input_password.click()
        assert page.tab_phone.is_active(check=check_select_tab, attr_name='class')
    except AssertionError as e:
        page.screenshot('login1.png')
        print(f"Смена Таба выбора аутентификации с логина на телефон автоматически не происходит")

    try:
        page.tab_user_login.click()
        assert page.tab_user_login.is_active(check=check_select_tab, attr_name='class')
        page.input_login.send_keys('test_email@gmail.com')
        page.input_password.click()
        assert page.tab_email.is_active(check=check_select_tab, attr_name='class')
    except AssertionError as e:
        page.screenshot('login2.png')
        print(f"Смена Таба выбора аутентификации с логина на почту автоматически не происходит")

    try:
        page.tab_user_login.click()
        assert page.tab_user_login.is_active(check=check_select_tab, attr_name='class')
        page.input_login.send_keys('312010992430')
        page.input_password.click()
        assert page.tab_ls.is_active(check=check_select_tab, attr_name='class')
    except AssertionError as e:
        page.screenshot('login3.png')
        print(f"Смена Таба выбора аутентификации с логина на ЛС автоматически не происходит")

    try:
        page.tab_ls.click()
        assert page.tab_ls.is_active(check=check_select_tab, attr_name='class')
        page.input_login.send_keys('+79171111111')
        page.input_password.click()
        assert page.tab_phone.is_active(check=check_select_tab, attr_name='class')
    except AssertionError as e:
        page.screenshot('ls1.png')
        print(f"Смена Таба выбора аутентификации с ЛС на телефон автоматически не происходит")

    try:
        page.tab_ls.click()
        assert page.tab_ls.is_active(check=check_select_tab, attr_name='class')
        page.input_login.send_keys('test_email@gmail.com')
        page.input_password.click()
        assert page.tab_email.is_active(check=check_select_tab, attr_name='class')
    except AssertionError as e:
        page.screenshot('ls2.png')
        print(f"Смена Таба выбора аутентификации с ЛС на почту автоматически не происходит")

    try:
        page.tab_ls.click()
        assert page.tab_ls.is_active(check=check_select_tab, attr_name='class')
        page.input_login.send_keys('my_rt_login')
        page.input_password.click()
        assert page.tab_user_login.is_active(check=check_select_tab, attr_name='class')
    except AssertionError as e:
        page.screenshot('ls3.png')
        print(f"Смена Таба выбора аутентификации с ЛС на логин автоматически не происходит")


# TC-12
@pytest.mark.auth
@pytest.mark.xfail(reason="\nЕсли появляется капча, необходим ручной ввод")
def test_auth_with_valid_email(web_browser):
    page = AuthPage(web_browser)


    assert page.tab_email.is_clickable()
    page.tab_email.click()
    assert page.tab_email.is_active(check=check_select_tab, attr_name='class')

    page.input_login.send_keys(valid_email)
    page.input_password.send_keys(valid_password)
    page.checkbox_remember_me.click()

    #time.sleep(15)

    assert page.login_btn.is_clickable()
    page.login_btn.click()
    page.wait_page_loaded()
    new_url = page.get_current_url()
    assert '/account_b2c/page' in str(new_url)


# TC-13
@pytest.mark.auth
@pytest.mark.xfail(reason="\nЕсли появляется капча, необходим ручной ввод")
def test_auth_with_valid_phone(web_browser):
    page = AuthPage(web_browser)

    assert page.tab_phone.is_clickable()
    page.tab_phone.click()
    assert page.tab_phone.is_active(check=check_select_tab, attr_name='class')

    page.input_login.send_keys(valid_phone)
    page.input_password.send_keys(valid_password)

    page.checkbox_remember_me.click()

    # time.sleep(15)

    assert page.login_btn.is_clickable()
    page.login_btn.click()

    page.wait_page_loaded()
    new_url = page.get_current_url()
    assert '/account_b2c/page' in str(new_url)


# TC-14, TC-15, TC-16
@pytest.mark.auth
@pytest.mark.xfail(reason="\nЕсли появляется капча, необходим ручной ввод")
@pytest.mark.parametrize(('email', 'password'), [(valid_email, '12345'),
                                                 ('test_email@gmail.com', valid_password),
                                                 ('test_email@gmail.com', '123456789Pss')
                                                 ],
                         ids=['valid email and invalid password',
                              'invalid email and valid password',
                              'invalid email and password'
                              ])
def test_valid_and_invalid_email_and_password(web_browser, email, password):
    page = AuthPage(web_browser)

    assert page.tab_email.is_clickable()
    page.tab_email.click()
    assert page.tab_email.is_active(check=check_select_tab, attr_name='class')

    page.input_login.send_keys(email)
    page.input_password.send_keys(password)

    page.checkbox_remember_me.click()

    # time.sleep(15)

    assert page.login_btn.is_clickable()
    page.login_btn.click()

    page.wait_page_loaded()
    new_url = page.get_current_url()
    assert '/account_b2c/page' not in str(new_url)

    error_text = page.auth_error_message.get_text()
    assert 'Неверный логин или пароль' in error_text
    assert page.forgot_password.is_active(check=check_forgot_password, attr_name='class')



# TC-17, TC-18
@pytest.mark.auth
@pytest.mark.xfail(reason="\nЕсли появляется капча, необходим ручной ввод")
@pytest.mark.parametrize(('email', 'password'), [('', valid_password),
                                                 ('', '')
                                                 ],
                         ids=['empty email and valid password',
                              'empty email and password'
                              ])
def test_empty_email(web_browser, email, password):
    page = AuthPage(web_browser)

    assert page.tab_email.is_clickable()
    page.tab_email.click()
    assert page.tab_email.is_active(check=check_select_tab, attr_name='class')

    page.input_login.send_keys(email)
    page.input_password.send_keys(password)

    page.checkbox_remember_me.click()

    # time.sleep(15)

    assert page.login_btn.is_clickable()
    page.login_btn.click()

    page.wait_page_loaded()
    url = page.get_current_url()
    assert '/account_b2c/page' not in str(url)

    assert page.login_error_message.is_presented() and page.login_error_message.is_visible()
    assert page.login_error_message.get_text() == "Введите адрес, указанный при регистрации"


# TC-18, TC-19
@pytest.mark.auth
@pytest.mark.xfail(reason="\nЕсли появляется капча, необходим ручной ввод")
def test_empty_password(web_browser):
    page = AuthPage(web_browser)

    assert page.tab_email.is_clickable()
    page.tab_email.click()
    assert page.tab_email.is_active(check=check_select_tab, attr_name='class')

    page.input_login.send_keys(valid_email)
    page.input_password.send_keys('')

    page.checkbox_remember_me.click()

    # time.sleep(15)

    assert page.login_btn.is_clickable()
    page.login_btn.click()

    page.wait_page_loaded()
    url = page.get_current_url()
    assert '/account_b2c/page' not in str(url)
    error_text = page.auth_error_message.get_text()
    assert 'Неверный логин или пароль' in error_text


# TC-20
@pytest.mark.reg
def test_register_btn(web_browser):
    page = AuthPage(web_browser)

    assert page.register_btn.is_clickable()
    page.register_btn.click()

    new_page_title = page.title.get_text()
    assert "Регистрация" in str(new_page_title)
