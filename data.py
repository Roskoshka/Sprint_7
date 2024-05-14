from faker import Faker

from helpers import register_new_courier_and_return_login_password, generate_random_string_for_test_data
fake = Faker()

# Уже созданный курьер
BODY_ALREADY_CREATED_COURIER = {
    'login': register_new_courier_and_return_login_password()[0],
    'password': register_new_courier_and_return_login_password()[1],
    'firstName': register_new_courier_and_return_login_password()[2]
}
# Рандомные данные для создания курьера
BODY_CREATE_COURIER = {
    'login': generate_random_string_for_test_data(10),
    'password': generate_random_string_for_test_data(10),
    'firstName': generate_random_string_for_test_data(10)
}
# Тело для запроса создания курьера без логина
BODY_CREATE_COURIER_WITHOUT_LOGIN = {
    'password': generate_random_string_for_test_data(10),
    'firstName': generate_random_string_for_test_data(10)
}
# Тело для запроса создания курьера с пустым логином
BODY_CREATE_COURIER_EMPTY_LOGIN = {
    'login': "",
    'password': generate_random_string_for_test_data(10),
    'firstName': generate_random_string_for_test_data(10)
}
# Тело для запроса создания курьера без пароля
BODY_CREATE_COURIER_WITHOUT_PASSWORD = {
    'login': generate_random_string_for_test_data(10),
    'firstName': generate_random_string_for_test_data(10)
}
# Тело для запроса создания курьера с пустым паролем
BODY_CREATE_COURIER_EMPTY_PASSWORD = {
    'login': generate_random_string_for_test_data(10),
    'password': "",
    'firstName': generate_random_string_for_test_data(10)
}
# Тело для запроса логина курьера без логина
BODY_LOGIN_COURIER_WITHOUT_LOGIN = {
    'password': register_new_courier_and_return_login_password()[1]
}
# Тело для запроса логина курьера с пустым логином
BODY_LOGIN_COURIER_EMPTY_LOGIN = {
    'login': "",
    'password': register_new_courier_and_return_login_password()[1]
}
# Тело для запроса логина курьера с пустым паролем
BODY_LOGIN_COURIER_EMPTY_PASSWORD = {
    'login': register_new_courier_and_return_login_password()[0],
    'password': ""
}
# Рандомные данные для логина несуществующего курьера
BODY_LOGIN_COURIER_NOT_FOUND = {
    'login': generate_random_string_for_test_data(10),
    'password': generate_random_string_for_test_data(10)
}
# Тело для успешного заказа с одним цветом
BODY_CREATE_ORDER_ONE_COLOR = {
    "firstName": fake.name(),
    "lastName": fake.last_name(),
    "address": fake.address(),
    "metroStation": "2",
    "phone": fake.phone_number(),
    "rentTime": 1,
    "deliveryDate": "2024-05-12T21:00:00.000Z",
    "comment": fake.word(),
    "color": ["BLACK"]
}

# Тело для успешного заказа с двумя цветами
BODY_CREATE_ORDER_TWO_COLORS = {
    "firstName": fake.name(),
    "lastName": fake.last_name(),
    "address": fake.address(),
    "metroStation": "3",
    "phone": fake.phone_number(),
    "rentTime": 2,
    "deliveryDate": "2024-05-12T21:00:00.000Z",
    "comment": fake.word(),
    "color": ["BLACK", "GREY"]
}

# Тело для успешного заказа с двумя цветами
BODY_CREATE_ORDER_WITHOUT_COLORS = {
    "firstName": fake.name(),
    "lastName": fake.last_name(),
    "address": fake.address(),
    "metroStation": "4",
    "phone": fake.phone_number(),
    "rentTime": 3,
    "deliveryDate": "2024-05-12T21:00:00.000Z",
    "comment": fake.word()
}

# Проверки в тестах
# Создание курьера - запрос с повторяющимся логином
CHECK_COURIER_CONFLICT = "Этот логин уже используется. Попробуйте другой."
# Создание курьера - запрос без логина или пароля
CHECK_CREATE_COURIER_BAD_REQUEST = "Недостаточно данных для создания учетной записи"
# Логин курьера - запрос с несуществующей парой логин-пароль
CHECK_LOGIN_COURIER_NOT_FOUND = "Учетная запись не найдена"
# Логин курьера - запрос без логина или пароля
CHECK_LOGIN_COURIER_BAD_REQUEST = "Недостаточно данных для входа"
