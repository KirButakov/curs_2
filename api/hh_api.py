import requests
from api.abstract_api import AbstractAPI

class HeadHunterAPI(AbstractAPI):
    """Класс для работы с API hh.ru."""

    def __init__(self):
        self.__base_url = "https://api.hh.ru/vacancies"

    def connect(self) -> bool:
        """Реализация абстрактного метода connect."""
        return self.__connect()

    def __connect(self) -> bool:
        """Приватный метод для подключения к API."""
        response = requests.get(self.__base_url)
        if response.status_code != 200:
            raise ConnectionError(f"Ошибка подключения: {response.status_code}")
        return True

    def get_vacancies(self, keyword: str) -> list:
        """Получение вакансий по ключевому слову."""
        self.connect()
        params = {
            "text": keyword,
            "per_page": 100
        }
        response = requests.get(self.__base_url, params=params)
        if response.status_code == 200:
            return response.json().get("items", [])
        return []
