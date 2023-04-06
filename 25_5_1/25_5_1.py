import pytest
from settings import valid_email, valid_password
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


def test_show_my_pets():
   pytest.driver.implicitly_wait(10)
   # Вводим email
   pytest.driver.find_element(By.ID, 'email').send_keys(valid_email)
   # Вводим пароль
   pytest.driver.find_element(By.ID, 'pass').send_keys(valid_password)
   # Нажимаем на кнопку входа в аккаунт
   pytest.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

   # Проверяем, что мы оказались на главной странице пользователя
   assert pytest.driver.find_element(By.TAG_NAME, 'h1').text == "PetFriends"

   images = pytest.driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-img-top')
   names = pytest.driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-title')
   descriptions = pytest.driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-text')

   for i in range(len(names)):
      #assert images[i].get_attribute('src') != ''
      assert names[i].text != ''
      assert descriptions[i].text != ''
      assert ', ' in descriptions[i]
      parts = descriptions[i].text.split(", ")
      assert len(parts[0]) > 0
      assert len(parts[1]) > 0

# 1 Проверяем, что присутствуют все питомцы
def test_all_pets_shown(all_my_pets):
   pytest.driver.implicitly_wait(10)
   user_pets = pytest.driver.find_elements(By.CSS_SELECTOR, ".\\.col-sm-4.left")

   pets = pytest.driver.find_elements(By.CSS_SELECTOR, '.table.table-hover tbody tr')

   number = user_pets[0].text.split('\n')
   number = number[1].split(' ')
   number = int(number[1])
   number_of_pets = len(pets)
   assert number == number_of_pets


# 2 Проверяем, что хотя бы у половины питомцев есть фото
def test_photo_availability(all_my_pets):

   pytest.driver.implicitly_wait(10)

   user_pets = pytest.driver.find_elements(By.CSS_SELECTOR, ".\\.col-sm-4.left")
   images = pytest.driver.find_elements(By.CSS_SELECTOR, '.table.table-hover img')

   number = user_pets[0].text.split('\n')
   number = number[1].split(' ')
   number = int(number[1])

   number_photos = 0
   for i in range(len(images)):
      if images[i].get_attribute('src') != '':
         number_photos += 1
   assert number_photos >= (number // 2)


# 3 Проверяем, что у всех питомцев есть имя, возраст и порода
def test_presence_name_age_and_gender(all_my_pets):
   pytest.driver.implicitly_wait(10)

   names = pytest.driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-title')
   descriptions = pytest.driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-text')

   for i in range(len(names)):
      assert names[i].text != ''
      assert descriptions[i].text != ''
      assert ', ' in descriptions[i]
      parts = descriptions[i].text.split(", ")
      assert len(parts[0]) > 0
      assert len(parts[1]) > 0


# 4 Проверяем, что у всех питомцев разные имена
def test_pet_names_differ(all_my_pets):
   pytest.driver.implicitly_wait(10)

   my_pets = pytest.driver.find_elements(By.XPATH, '//*[@id="all_my_pets"]/table/tbody/tr')
   pet_name = [pet.text.split(' ')[0] for pet in my_pets]
   print('\nСписок имен : ', pet_name)
   assert len(set(pet_name)) == len(pet_name)


# 5 Проверяем, что в списке нет повторяющихся питомцев
def test_no_duplicate_pets(all_my_pets):
   pytest.driver.implicitly_wait(10)

   my_pets = pytest.driver.find_elements(By.XPATH, '//*[@id="all_my_pets"]/table/tbody/tr')

   # список c данными наших питомцев
   pets_info = [pet.text for pet in my_pets]
   #print('\nДанные питомцев : ', pets_info)
   assert len(my_pets) == len(set(pets_info))
