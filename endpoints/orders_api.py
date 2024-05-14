import allure
import requests

import urls


class OrdersApi:
    @staticmethod
    @allure.step("Отправка запроса на создание заказа")
    def create_order(body):
        return requests.post(urls.BASE_URL + urls.CREATE_ORDER_ENDPOINT, json=body)

    @staticmethod
    @allure.step("Отправка запроса на получение списка заказов")
    def get_list_of_orders():
        return requests.get(urls.BASE_URL + urls.LIST_OF_ORDERS_ENDPOINT)
