import unittest
from api.hh_api import HeadHunterAPI

class TestHeadHunterAPI(unittest.TestCase):
    def setUp(self):
        self.api = HeadHunterAPI()

    def test_get_vacancies(self):
        """Тест получения вакансий."""
        vacancies = self.api.get_vacancies("Python")
        self.assertIsInstance(vacancies, list)
        self.assertTrue(len(vacancies) > 0)

    def test_connect(self):
        """Тест подключения к API."""
        self.assertTrue(self.api.connect())

if __name__ == "__main__":
    unittest.main()
