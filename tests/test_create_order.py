import allure
import pytest

import data
from endpoints.orders_api import OrdersApi


class TestCreateOrder:
    @allure.title('Успешное создание заказа.')
    @allure.description('Проверка успешного создания заказа. '
                        'Получаем статус 201 и track в теле ответа.')
    @pytest.mark.parametrize("body", [data.BODY_CREATE_ORDER_ONE_COLOR,
                                      data.BODY_CREATE_ORDER_TWO_COLORS,
                                      data.BODY_CREATE_ORDER_WITHOUT_COLORS])
    def test_login_courier_success(self, body):
        response_create_order_one_color = OrdersApi.create_order(body)

        assert (response_create_order_one_color.status_code == 201
                and response_create_order_one_color.json()['track'] is not None
                and response_create_order_one_color.json()['track'] > 0)
