import unittest
import os
import json
from vacancies.vacancy import Vacancy
from file_handlers.json_handler import JSONHandler

class TestJSONHandler(unittest.TestCase):
    def setUp(self):
        self.filename = "test_vacancies.json"
        self.handler = JSONHandler(self.filename)
        self.vacancy = Vacancy(
            "Python Developer",
            "https://hh.ru/vacancy/123456",
            "100000-150000 руб.",
            "Требования: опыт работы от 3 лет..."
        )

    def tearDown(self):
        if os.path.exists(self.filename):
            os.remove(self.filename)

    def test_add_vacancy(self):
        """Тест добавления вакансии в JSON-файл."""
        self.handler.add_vacancy(self.vacancy)
        with open(self.filename, "r") as file:
            data = json.load(file)
            self.assertEqual(len(data), 1)
            self.assertEqual(data[0]["title"], "Python Developer")

    def test_get_vacancies(self):
        """Тест получения вакансий из JSON-файла."""
        self.handler.add_vacancy(self.vacancy)
        vacancies = self.handler.get_vacancies(lambda x: True)
        self.assertEqual(len(vacancies), 1)
        self.assertEqual(vacancies[0]["title"], "Python Developer")

    def test_delete_vacancy(self):
        """Тест удаления вакансии из JSON-файла."""
        self.handler.add_vacancy(self.vacancy)
        self.handler.delete_vacancy(self.vacancy)
        with open(self.filename, "r") as file:
            data = json.load(file)
            self.assertEqual(len(data), 0)

if __name__ == "__main__":
    unittest.main()