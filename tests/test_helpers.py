import unittest
from vacancies.vacancy import Vacancy
from utils.helpers import filter_vacancies, sort_vacancies, get_top_vacancies

class TestHelpers(unittest.TestCase):
    def setUp(self):
        self.vacancies = [
            Vacancy("Python Developer", "https://hh.ru/vacancy/1", "100000", "Требования: Python, Django"),
            Vacancy("Backend Developer", "https://hh.ru/vacancy/2", "120000", "Требования: Python, Flask"),
            Vacancy("Junior Python Developer", "https://hh.ru/vacancy/3", "80000", "Требования: Python, обучение"),
        ]

    def test_filter_vacancies(self):
        """Тест фильтрации вакансий по ключевым словам."""
        filtered = filter_vacancies(self.vacancies, ["Django"])
        self.assertEqual(len(filtered), 1)
        self.assertEqual(filtered[0].title, "Python Developer")

    def test_sort_vacancies(self):
        """Тест сортировки вакансий по зарплате."""
        sorted_vacancies = sort_vacancies(self.vacancies)
        self.assertEqual(sorted_vacancies[0].salary, "120000")
        self.assertEqual(sorted_vacancies[1].salary, "100000")
        self.assertEqual(sorted_vacancies[2].salary, "80000")

    def test_get_top_vacancies(self):
        """Тест получения топ-N вакансий."""
        top_vacancies = get_top_vacancies(self.vacancies, 2)
        self.assertEqual(len(top_vacancies), 2)
        self.assertEqual(top_vacancies[0].title, "Python Developer")
        self.assertEqual(top_vacancies[1].title, "Backend Developer")

if __name__ == "__main__":
    unittest.main()