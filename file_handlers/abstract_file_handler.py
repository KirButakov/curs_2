from abc import ABC, abstractmethod

class AbstractFileHandler(ABC):
    """Абстрактный класс для работы с файлами."""

    @abstractmethod
    def add_vacancy(self, vacancy) -> None:
        """Добавление вакансии в файл."""
        pass

    @abstractmethod
    def get_vacancies(self, criteria: callable) -> list:
        """Получение вакансий по критерию."""
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy) -> None:
        """Удаление вакансии из файла."""
        pass
