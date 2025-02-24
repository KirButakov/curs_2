import unittest
from vacancies.vacancy import Vacancy

class TestVacancy(unittest.TestCase):
    def setUp(self):
        self.vacancy = Vacancy(
            "Python Developer",
            "https://hh.ru/vacancy/123456",
            "100000-150000 руб.",
            "Требования: опыт работы от 3 лет..."
        )

    def test_vacancy_creation(self):
        """Тест создания вакансии."""
        self.assertEqual(self.vacancy.title, "Python Developer")
        self.assertEqual(self.vacancy.link, "https://hh.ru/vacancy/123456")
        self.assertEqual(self.vacancy.salary, "100000-150000 руб.")
        self.assertEqual(self.vacancy.description, "Требования: опыт работы от 3 лет...")

    def test_validate_salary(self):
        """Тест валидации зарплаты."""
        vacancy = Vacancy("Test", "https://test.com", "", "Test")
        self.assertEqual(vacancy.salary, "Зарплата не указана")

    def test_to_dict(self):
        """Тест преобразования вакансии в словарь."""
        expected_dict = {
            "title": "Python Developer",
            "link": "https://hh.ru/vacancy/123456",
            "salary": "100000-150000 руб.",
            "description": "Требования: опыт работы от 3 лет..."
        }
        self.assertEqual(self.vacancy.to_dict(), expected_dict)

    def test_cast_to_object_list(self):
        """Тест преобразования списка словарей в список объектов Vacancy."""
        vacancies_data = [
            {
                "name": "Python Developer",
                "alternate_url": "https://hh.ru/vacancy/123456",
                "salary": {"from": 100000, "to": 150000},
                "snippet": {"requirement": "Требования: опыт работы от 3 лет..."}
            }
        ]
        vacancies = Vacancy.cast_to_object_list(vacancies_data)
        self.assertIsInstance(vacancies, list)
        self.assertEqual(len(vacancies), 1)
        self.assertEqual(vacancies[0].title, "Python Developer")

if __name__ == "__main__":
    unittest.main()