import allure
import pytest

import data
from endpoints.courier_api import CourierApi


class TestCreateCourier:
    @allure.title('Успешное создание курьера.')
    @allure.description('Проверка успешного создания курьера. Получаем статус 201 и тело ответа: {ok: true}.')
    def test_create_courier_success(self, default_courier):
        response_create_courier = CourierApi.create_courier(default_courier)

        assert (response_create_courier.status_code == 201 and response_create_courier.json()['ok'] == True)

    @allure.title('Нельзя создать двух одинаковых курьеров.')
    @allure.description('Проверка создания уже существующего курьера. Получаем статус код 409 и сообщение.')
    def test_create_courier_conflict(self, default_courier):
        CourierApi.create_courier(default_courier)
        response_create_courier_conflict = CourierApi.create_courier(default_courier)

        assert (response_create_courier_conflict.status_code == 409
                and response_create_courier_conflict.json()['message'] == data.CHECK_COURIER_CONFLICT)

    @allure.title('Ошибка при создании курьера без одного из обязательных параметров.')
    @allure.description('Проверка создания курьера, если не передан один из обязательных параметров.')
    @pytest.mark.parametrize("body", [data.BODY_CREATE_COURIER_WITHOUT_LOGIN,
                                      data.BODY_CREATE_COURIER_EMPTY_LOGIN,
                                      data.BODY_CREATE_COURIER_WITHOUT_PASSWORD,
                                      data.BODY_CREATE_COURIER_EMPTY_PASSWORD])
    def test_create_courier_bad_request(self, body):
        response_create_courier_bad_request = CourierApi.create_courier(body)

        assert (response_create_courier_bad_request.status_code == 400
                and response_create_courier_bad_request.json()['message'] == data.CHECK_CREATE_COURIER_BAD_REQUEST)
