from api.hh_api import HeadHunterAPI
from vacancies.vacancy import Vacancy
from file_handlers.json_handler import JSONHandler
from file_handlers.csv_handler import CSVHandler
from utils.helpers import filter_vacancies, sort_vacancies, get_top_vacancies

def user_interaction():
    """Функция для взаимодействия с пользователем."""
    hh_api = HeadHunterAPI()
    search_query = input("Введите поисковый запрос: ")
    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()

    # Получаем вакансии
    hh_vacancies = hh_api.get_vacancies(search_query)
    print(f"Найдено вакансий: {len(hh_vacancies)}")  # Вывод количества вакансий

    # Преобразуем данные в объекты Vacancy
    vacancies_list = Vacancy.cast_to_object_list(hh_vacancies)
    print(f"Преобразовано в объекты: {len(vacancies_list)}")  # Вывод количества объектов



    # Фильтрация вакансий
    filtered_vacancies = filter_vacancies(vacancies_list, filter_words)
    print(f"\nОтфильтровано вакансий: {len(filtered_vacancies)}")  # Вывод количества отфильтрованных вакансий

    # Сортировка вакансий
    sorted_vacancies = sort_vacancies(filtered_vacancies)
    print(f"Отсортировано вакансий: {len(sorted_vacancies)}")  # Вывод количества отсортированных вакансий

    # Получение топ-N вакансий
    top_vacancies = get_top_vacancies(sorted_vacancies, top_n)
    print(f"Топ-{top_n} вакансий: {len(top_vacancies)}")  # Вывод количества топ-N вакансий

    # Сохранение вакансий в файлы
    json_saver = JSONHandler()
    csv_saver = CSVHandler()

    for vacancy in top_vacancies:
        json_saver.add_vacancy(vacancy)
        csv_saver.add_vacancy(vacancy)

    # Вывод вакансий в консоль
    print("\nРезультаты:")
    for i, vacancy in enumerate(top_vacancies, 1):
        print(f"\nВакансия #{i}")
        print(f"  Название: {vacancy.title}")
        print(f"  Ссылка: {vacancy.link}")
        print(f"  Зарплата: {vacancy.salary}")
        print(f"  Описание: {vacancy.description}")
        print("-" * 40)

if __name__ == "__main__":
    user_interaction()
