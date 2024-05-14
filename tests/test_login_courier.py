import allure
import pytest

import data
from endpoints.courier_api import CourierApi


class TestLoginCourier:
    @allure.title('Успешный логин курьера.')
    @allure.description('Проверка успешного логина курьера. Получаем статус 200 и id в теле ответа.')
    def test_login_courier_success(self, default_courier):
        CourierApi.create_courier(default_courier)
        response_login_courier = CourierApi.login_courier(default_courier)
        courier_id = response_login_courier.json()['id']

        assert (response_login_courier.status_code == 200 and courier_id is not None and courier_id > 0)

    @allure.title('Нельзя создать двух одинаковых курьеров.')
    @allure.description('Проверка создания уже существующего курьера. Получаем статус код 409 и сообщение.')
    def test_login_courier_not_found(self):
        response_login_courier_not_found = CourierApi.login_courier(data.BODY_LOGIN_COURIER_NOT_FOUND)

        assert (response_login_courier_not_found.status_code == 404
                and response_login_courier_not_found.json()['message'] == data.CHECK_LOGIN_COURIER_NOT_FOUND)

    @allure.title('Ошибка при логине курьера без одного из обязательных параметров.')
    @allure.description('Проверка логина курьера, если не передан один из обязательных параметров.')
    @pytest.mark.parametrize("body", [data.BODY_LOGIN_COURIER_WITHOUT_LOGIN,
                                      data.BODY_LOGIN_COURIER_EMPTY_LOGIN,
                                      data.BODY_LOGIN_COURIER_EMPTY_PASSWORD])
    def test_login_courier_bad_request(self, body):
        CourierApi.create_courier(body)
        response_login_courier_bad_request = CourierApi.login_courier(body)

        assert (response_login_courier_bad_request.status_code == 400
                and response_login_courier_bad_request.json()['message'] == data.CHECK_LOGIN_COURIER_BAD_REQUEST)
