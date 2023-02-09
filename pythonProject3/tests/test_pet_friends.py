from api import PetFriends
from settings import valid_email, valid_password, empty_email, empty_password, \
                     invalid_email, invalid_password
import os

pf = PetFriends()


def test_get_api_key_for_valid_user(email=valid_email, password=valid_password):
    """ Проверяем что запрос api ключа возвращает статус 200 и в тезультате содержится слово key"""

    status, result = pf.get_api_key(email, password)

    assert status == 200
    assert 'key' in result


def test_get_all_pets_with_valid_key(filter=''):
    """ Проверяем что запрос всех питомцев возвращает не пустой список.
    Для этого сначала получаем api ключ и сохраняем в переменную auth_key. Далее используя этого ключ
    запрашиваем список всех питомцев и проверяем что список не пустой"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_list_of_pets(auth_key, filter)

    assert status == 200
    assert len(result['pets']) > 0
    print(result)


def test_add_new_pet_with_valid_data(name='Барбоскин', animal_type='двортерьер',
                                     age='4', pet_photo='images/cat1.jpeg'):
    """Проверяем что можно добавить питомца с корректными данными"""

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result['name'] == name


def test_successful_delete_self_pet():
    """Проверяем возможность удаления питомца"""

    # Получаем ключ auth_key и запрашиваем список своих питомцев
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Проверяем - если список своих питомцев пустой, то добавляем нового и опять запрашиваем список своих питомцев
    if len(my_pets['pets']) == 0:
        pf.add_new_pet(auth_key, "Суперкот", "кот", "3", "images/cat1.jpeg")
        _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Берём id первого питомца из списка и отправляем запрос на удаление
    pet_id = my_pets['pets'][0]['id']
    status, _ = pf.delete_pet(auth_key, pet_id)

    # Ещё раз запрашиваем список своих питомцев
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Проверяем что статус ответа равен 200 и в списке питомцев нет id удалённого питомца
    assert status == 200
    assert pet_id not in my_pets.values()


def test_successful_update_self_pet_info(name='Мурзик', animal_type='Котэ', age=5):
    """Проверяем возможность обновления информации о питомце"""

    # Получаем ключ auth_key и список своих питомцев
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Еслди список не пустой, то пробуем обновить его имя, тип и возраст
    if len(my_pets['pets']) > 0:
        status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)

        # Проверяем что статус ответа = 200 и имя питомца соответствует заданному
        assert status == 200
        assert result['name'] == name
    else:
        # если спиок питомцев пустой, то выкидываем исключение с текстом об отсутствии своих питомцев
        raise Exception("There are no my pets")


# 1
def test_get_api_key_no_password(email=valid_email, password=empty_password):
    """Проверяем, что при отсутствии пароля запрос api возвращает статус 403
     и в результате не содержится слово key"""

    status, result = pf.get_api_key(email, password)

    assert status == 403
    assert 'key' not in result


# 2
def test_get_api_key_no_email(email=empty_email, password=valid_password):
    """Проверяем, что при пустом поле email запрос api возвращает статус 403
     и в результате не содержится слово key"""

    status, result = pf.get_api_key(email, password)

    assert status == 403
    assert 'key' not in result


# 3
def test_get_api_key_wrong_user(email=invalid_email, password=invalid_password):
    """Проверяем, что при вводе неправильного email и пароля запрос api возвращает
     статус 403 и в результате не содержится слово key"""

    status, result = pf.get_api_key(email, password)

    assert status == 403
    assert 'key' not in result


# 4
def test_get_api_key_no_user_input(email=empty_email, password=empty_password):
    """Проверяем, что при не заполненных полях email b пароль запрос api возвращает
     статус 403 и в результате не содержится слово key"""

    status, result = pf.get_api_key(email, password)

    assert status == 403
    assert 'key' not in result


# 5
def test_get_list_my_pets_with_valid_key(filter='my_pets'):
    """ Проверяем, что запрос списка питомцев в фильтре возвращает список.
    Для этого сначала получаем api ключ и сохраняем в переменную auth_key. Далее, используя этот ключ,
    запрашиваем список питомцев и проверяем список.
    Значение параметра filter - 'my_pets' (питомцы пользователя) """

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_list_of_pets(auth_key, filter)

    if len(result['pets']) > 0:
        assert status == 200
        print(result)
    else:
        assert status == 200
        print('There is not any pet')


# 6
def test_get_list_my_pets_with_unvalid_key(filter=''):
    """ Проверяем, что запрос списка питомцев с невалидным ключом запрос
        возвращает 403 статус, доступа нет. """

    auth_key = {'key': '8661166bbf6792c8e46dc4309d0fa3a4d27ca40fe54f6967f61b78'}
    status, result = pf.get_list_of_pets(auth_key, filter)

    assert status == 403
    assert 'Forbidden' in result


# 7
def test_add_new_pet_with_invalid_key(name='Барбоскин', animal_type='пес',
                                      age='4', pet_photo='images/cat2.jpeg'):
    """Добавляем нового питомца, используя невалидный ключ. Проверяем, что
        запрос возвращает статус 403"""

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    auth_key = {'key': '8661166bbf6792c8e46dc4309d0fa3a4d27ca40fe54f6967f61b78'}
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    assert status == 403
    assert 'Forbidden' in result


# 8
def test_add_new_pet_without_photo_valid_key(name='Матроскин', animal_type='кот', age='7'):
    """Проверяем, что можно добавить питомца без фото с корректными данными,
     запрос возвращает статус 200"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)

    status, result = pf.add_new_pet_without_photo(auth_key, name, animal_type, age)

    assert status == 200
    assert result['name'] == name
    assert result['pet_photo'] == ''


# 9
def test_add_new_pet_without_photo_invalid_key(name='Матроскин', animal_type='кот', age='7'):
    """Проверяем, что нельзя добавить питомца без фото с невалидным ключом"""

    auth_key = {'key': '8661166bbf6792c8e46dc4309d0fa3a4d27ca40fe54f6967f61b78'}
    status, result = pf.add_new_pet_without_photo(auth_key, name, animal_type, age)

    assert status == 403
    assert 'Forbidden' in result


# 10
def test_add_pet_photo(pet_photo='images/cat2.jpeg'):
    """Проверяем что можно добавить или заменить фото питомца с корректными данными"""

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Проверяем - если список питомцев пустой, то добавляем нового и опять запрашиваем список
    if len(my_pets['pets']) == 0:

        pf.add_new_pet_without_photo(auth_key, "Мурзик", "кот", "7")
        _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")\

    pet_id = my_pets['pets'][0]['id']

    status, result = pf.add_pet_photo(auth_key, pet_id, pet_photo)

    assert status == 200
    assert 'pet_photo' in result
