class Vacancy:
    """Класс для представления вакансии."""

    __slots__ = ["title", "link", "salary", "description"]

    def __init__(self, title: str, link: str, salary: str, description: str):
        """
        Инициализация вакансии.
        :param title: Название вакансии.
        :param link: Ссылка на вакансию.
        :param salary: Зарплата.
        :param description: Описание вакансии.
        """
        self.title = title
        self.link = link
        self.salary = self.__validate_salary(salary)
        self.description = description

    def __validate_salary(self, salary: str) -> str:
        """Валидация зарплаты."""
        if not salary:
            return "Зарплата не указана"
        return salary

    def __eq__(self, other) -> bool:
        """Сравнение вакансий по зарплате (==)."""
        return self.salary == other.salary

    def __lt__(self, other) -> bool:
        """Сравнение вакансий по зарплате (<)."""
        return self.salary < other.salary

    def __gt__(self, other) -> bool:
        """Сравнение вакансий по зарплате (>)."""
        return self.salary > other.salary

    def __repr__(self) -> str:
        """Представление вакансии в виде строки."""
        return f"Vacancy(title={self.title}, salary={self.salary})"

    def to_dict(self) -> dict:
        """Преобразование объекта Vacancy в словарь."""
        return {
            "title": self.title,
            "link": self.link,
            "salary": self.salary,
            "description": self.description
        }

    @staticmethod
    def cast_to_object_list(vacancies_data: list) -> list:
        """Преобразование списка словарей в список объектов Vacancy."""
        vacancies = []
        for item in vacancies_data:
            salary = item.get("salary")
            if salary is not None:
                salary_from = str(salary.get("from", ""))
            else:
                salary_from = "Зарплата не указана"

            vacancy = Vacancy(
                item.get("name", ""),
                item.get("alternate_url", ""),
                salary_from,
                item.get("snippet", {}).get("requirement", "")
            )
            vacancies.append(vacancy)
        return vacancies
