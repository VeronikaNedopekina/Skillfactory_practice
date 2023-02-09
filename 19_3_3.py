import requests
import json


status = 'sold'
petID = '12345'


# GET finds pets by status
def find_pet_status():
    res = requests.get(f"https://petstore.swagger.io/v2/pet/findByStatus?status={status}",
                       headers={'accept': 'application/json'})
    result = ''
    try:
        result = res.json()
    except json.decoder.JSONDecodeError:
        result = res.text
    print(res.status_code)
    print(result)


# GET finds pet by ID
def find_pet_id():
    res = requests.get(f"https://petstore.swagger.io/v2/pet/{petID}",
                       headers={'accept': 'application/json'})
    result = ''
    try:
        result = res.json()
    except json.decoder.JSONDecodeError:
        result = res.text
    print(res.status_code)
    print(result)


# POST add a new pet
def add_new_pet():
    info = {
      "id": 12345,
      "category": {
        "id": 0,
        "name": "cat"
      },
      "name": "Murzik",
      "photoUrls": [
        "Murzik's photo"
      ],
      "tags": [
        {
          "id": 0,
          "name": "string"
        }
      ],
      "status": "available"
    }
    res = requests.post(f"https://petstore.swagger.io/v2/pet", headers={'accept': 'application/json',
                        'Content-Type': 'application/json'}, data=json.dumps(info, ensure_ascii=False))
    print(res.status_code)
    print(type(res.json()))


# PUT updates an existing pet
def update_pet():
    change_pet = {'name': 'bax', 'status': 'sold'}

    res = requests.put(f"https://petstore.swagger.io/v2/pet/",
                       headers={'accept': 'application/json', 'Content-Type': 'application/json'},
                       data=json.dumps(change_pet))

    print(res.status_code)
    print(type(res.json()))
    print(res.json())


# DELETE deletes a pet
def delete_pet():
    res = requests.delete(f'https://petstore.swagger.io/v2/pet/{petID}',
                          headers={'accept': 'application/json'})
    print(res.status_code)
    print(f'ID {petID}')


# add_new_pet()
# find_pet_status()
# find_pet_id()
# update_pet()
# delete_pet()
