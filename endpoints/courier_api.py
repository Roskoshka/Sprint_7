import allure
import requests
import urls


class CourierApi:
    @staticmethod
    @allure.step("Отправка запроса на создание курьера")
    def create_courier(body):
        return requests.post(urls.BASE_URL + urls.CREATE_COURIER_ENDPOINT, json=body)

    @staticmethod
    @allure.step("Отправка запроса на логин курьера")
    def login_courier(body):
        return requests.post(urls.BASE_URL + urls.LOGIN_COURIER_ENDPOINT, json=body)
