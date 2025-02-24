import csv
from file_handlers.abstract_file_handler import AbstractFileHandler

class CSVHandler(AbstractFileHandler):
    """Класс для работы с CSV-файлами."""

    def __init__(self, filename: str = "vacancies.csv"):
        self.__filename = filename

    def add_vacancy(self, vacancy) -> None:
        """Добавление вакансии в CSV-файл."""
        with open(self.__filename, "a+", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow([vacancy.title, vacancy.link, vacancy.salary, vacancy.description])

    def get_vacancies(self, criteria: callable) -> list:
        """Получение вакансий по критерию."""
        with open(self.__filename, "r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file)
            return [row for row in reader if criteria(row)]

    def delete_vacancy(self, vacancy) -> None:
        """Удаление вакансии из CSV-файла."""
        with open(self.__filename, "r", newline="", encoding="utf-8") as file:
            rows = list(csv.reader(file))
        rows = [row for row in rows if row != [vacancy.title, vacancy.link, vacancy.salary, vacancy.description]]
        with open(self.__filename, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerows(rows)
