import json
from file_handlers.abstract_file_handler import AbstractFileHandler

class JSONHandler(AbstractFileHandler):
    """Класс для работы с JSON-файлами."""

    def __init__(self, filename: str = "vacancies.json"):
        self.__filename = filename

    def add_vacancy(self, vacancy) -> None:
        """Добавление вакансии в JSON-файл."""
        with open(self.__filename, "a+") as file:
            file.seek(0)
            try:
                data = json.load(file)
            except (json.JSONDecodeError, FileNotFoundError):
                data = []
            if vacancy.to_dict() not in data:
                data.append(vacancy.to_dict())
            file.seek(0)
            file.truncate()
            json.dump(data, file, indent=4)

    def get_vacancies(self, criteria: callable) -> list:
        """Получение вакансий по критерию."""
        with open(self.__filename, "r") as file:
            data = json.load(file)
            return [item for item in data if criteria(item)]

    def delete_vacancy(self, vacancy) -> None:
        """Удаление вакансии из JSON-файла."""
        with open(self.__filename, "r") as file:
            data = json.load(file)
        data = [item for item in data if item != vacancy.to_dict()]
        with open(self.__filename, "w") as file:
            json.dump(data, file, indent=4)