from pages.base import WebPage
from pages.elements import WebElement, ManyWebElements


auth_url = 'https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/' \
           'auth?client_id=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/' \
           'login&response_type=code&scope=openid&state=65cadde0-21a9-40b4-831b-3a8b65fed795&theme&auth_type'

check_select_tab = 'rt-tab--active'
check_forgot_password = 'login-form__forgot-pwd--animated'


class AuthPage(WebPage):
    def __init__(self, web_driver, url=''):
        url = auth_url
        super().__init__(web_driver, url)

    logo = WebElement(css_selector='footer#app-footer>div>div')
    title = WebElement(css_selector='.card-container__title')
    tabs = ManyWebElements(css_selector='.rt-tab')
    tab_phone = WebElement(id='t-btn-tab-phone')
    tab_email = WebElement(id='t-btn-tab-mail')
    tab_user_login = WebElement(id='t-btn-tab-login')
    tab_ls = WebElement(id='t-btn-tab-ls')
    input_login = WebElement(id='username')
    input_login_title = WebElement(css_selector='div.tabs-input-container__login>div>span.rt-input__placeholder')
    input_password = WebElement(id='password')
    input_password_title = WebElement(css_selector='div.rt-input--actions>span.rt-input__placeholder')
    login_btn = WebElement(name='login')
    password_field = WebElement(name='password')
    checkbox_remember_me = WebElement(css_selector='.rt-checkbox')
    auth_error_message = WebElement(id='form-error-message')
    login_error_message = WebElement(css_selector='.rt-input-container__meta--error')
    forgot_password = WebElement(id='forgot_password')
    register_btn = WebElement(id='kc-register')
    user_name = WebElement(css_selector='div.user-info__name-container')
