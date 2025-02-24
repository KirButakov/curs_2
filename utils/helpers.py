from typing import List, Optional
from vacancies.vacancy import Vacancy

def filter_vacancies(vacancies: List[Vacancy], filter_words: List[str]) -> List[Vacancy]:
    """Фильтрация вакансий по ключевым словам (без учета регистра и с частичным совпадением)."""
    return [
        vacancy for vacancy in vacancies
        if any(word.lower() in vacancy.description.lower() for word in filter_words)
    ]

def sort_vacancies(vacancies: List[Vacancy]) -> List[Vacancy]:
    """Сортировка вакансий по зарплате (по убыванию)."""
    def get_salary_value(salary: Optional[str]) -> int:
        """Преобразует зарплату в число для корректной сортировки."""
        if salary is None or salary == "Зарплата не указана":
            return 0
        # Извлекаем первое число из строки (например, "100000-150000 руб." -> 100000)
        parts = salary.split("-")
        if parts:
            return int(parts[0].replace(" ", "").replace("руб.", ""))
        return 0

    return sorted(vacancies, key=lambda x: get_salary_value(x.salary), reverse=True)

def get_top_vacancies(vacancies: List[Vacancy], top_n: int) -> List[Vacancy]:
    """Получение топ-N вакансий."""
    return vacancies[:top_n]
