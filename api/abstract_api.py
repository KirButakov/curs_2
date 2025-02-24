from abc import ABC, abstractmethod
import requests

class AbstractAPI(ABC):
    """Абстрактный класс для работы с API."""

    @abstractmethod
    def connect(self) -> bool:
        """Подключение к API."""
        pass

    @abstractmethod
    def get_vacancies(self, keyword: str) -> list:
        """Получение вакансий по ключевому слову."""
        pass
