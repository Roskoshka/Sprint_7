import allure

from endpoints.orders_api import OrdersApi


class TestGetListOfOrders:
    @allure.title('Получение списка заказов')
    @allure.description('Проверка, что в тело возвращается список заказов.')
    def test_get_list_of_orders(self):
        response_get_list_of_orders = OrdersApi.get_list_of_orders()

        assert (response_get_list_of_orders.status_code == 200
                and response_get_list_of_orders.json()['orders'] is not None)
