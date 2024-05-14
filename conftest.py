import pytest
import requests
import urls
from data import BODY_CREATE_COURIER


# Фикстура - рандомные данные для создания курьера в тесте и удаление этого курьера в конце теста
@pytest.fixture(scope='function')
def default_courier():
    payload = BODY_CREATE_COURIER
    yield payload

    response_id = requests.post(urls.BASE_URL + urls.LOGIN_COURIER_ENDPOINT, data=payload)
    id_number = response_id.json()["id"]
    requests.delete(f"{urls.BASE_URL}{urls.DELETE_COURIER_ENDPOINT}{id_number}")
