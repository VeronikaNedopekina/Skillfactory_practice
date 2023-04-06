import pytest
import time
from settings import valid_email, valid_password
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


@pytest.fixture(autouse=True)
def testing():
   pytest.driver = webdriver.Chrome('/Users/veronikanedopekina/Downloads/chromedriver_mac64/chromedriver')
   pytest.driver.implicitly_wait(10)
   # Переходим на страницу авторизации
   pytest.driver.get('http://petfriends.skillfactory.ru/login')

   yield

   pytest.driver.quit()

@pytest.fixture()
def all_my_pets():

   # Вводим email
   WebDriverWait(pytest.driver, 5).until(
      EC.presence_of_element_located((By.ID, 'email'))).send_keys(valid_email)

   # Вводим пароль
   WebDriverWait(pytest.driver, 5).until(
      EC.presence_of_element_located((By.ID, 'pass'))).send_keys(valid_password)

   # Нажимаем на кнопку входа в аккаунт
   WebDriverWait(pytest.driver, 5).until(
      EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[type="submit"]'))).click()

   # Нажимаем на кнопку "Мои питомцы" для перехода на страницу с моими питомцами
   WebDriverWait(pytest.driver, 5).until(
      EC.element_to_be_clickable((By.XPATH, '//a[contains(text(),"Мои питомцы")]'))).click()
   time.sleep(1)
