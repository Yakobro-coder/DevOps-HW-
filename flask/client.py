import requests

HOST = 'http://127.0.0.1:5000/'

# GET запрос
response = requests.get(f'{HOST}adv')
print(response.json())

# POST запрос. Создание объявления
data = {
    'advertisement': {'title': "Sell garage",
                      'description': "Big, dry, with a pit. The light is on.",
                      },
    'user': {'login': 'yakobro',
             'email': 'yakobro@mail.ru',
             'phone': '8-800-555-35-35'}
}
response = requests.post(f'{HOST}create', json=data)
print(response.json())

# POST запрос. Проверка валидации
data_err = {
    'advertisement': {'title': 123,
                      'description': "test_valid",
                      },
    'user': {#'login': 'yakobro',
             #'email': 'yakobro@mail.ru',
             'phone': '8-800-555-35-35'}
}
response = requests.post(f'{HOST}create', json=data_err)
print(response.json())

# DELETE запрос
response = requests.delete(f'{HOST}adv/1')
print(response.json())
