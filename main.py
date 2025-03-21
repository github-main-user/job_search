#! /usr/bin/env python
from src.api import HeadHunterAPI
from src.vacancy import Vacancy

hh_api = HeadHunterAPI()


def print_vacancies(vacancies: list[Vacancy]) -> None:
    """Выводит вакансии в stdout."""
    print(f"\nПо данному запросу удалось найти {len(vacancies)} вакансий, с использованием API HeadHanter", end="\n\n")

    for vacancy in vacancies:
        print(vacancy, end="\n\n")


def user_interaction() -> None:
    search_query = input("Введите поисковый запрос: ")
    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    filter_word = input("Введите ключевое слово, для фильтрации по требованиям: ")

    # Получение вакансий
    vacancies_dict = hh_api.get_vacancies(search_query)

    # Преобразование в список объектов
    vacancies = Vacancy.cast_to_object_list(vacancies_dict)

    # Фильтрация по ключевому слову в описании
    if filter_word:
        vacancies = [vc for vc in vacancies if filter_word.lower() in vc.requirement.lower()]

    # Сортировка по зарплате
    vacancies.sort(key=lambda x: x.salary, reverse=True)

    # Вывод на экран
    print_vacancies(vacancies[:top_n])


if __name__ == "__main__":
    try:
        user_interaction()
    except KeyboardInterrupt:
        print()
