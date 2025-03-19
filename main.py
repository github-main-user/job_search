#! /usr/bin/env python
from src.api import HeadHunterAPI
from src.vacancy import Vacancy

hh_api = HeadHunterAPI()


def print_vacancies(vacancies: list[Vacancy]) -> None:
    """Выводит вакансии в stdout, при этом форматируя вывод."""
    print(f"\nПо данному запросу найдено {len(vacancies)}, с использованием API HeadHanter", end="\n\n")

    for vacancy in vacancies:
        print(vacancy, end="\n\n")


def user_interaction() -> None:
    search_query = input("Введите поисковый запрос: ")
    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    filter_word = input("Введите ключевое слово, для фильтрации по требованиям: ")

    # Получение вакансий
    vacancies_json = hh_api.get_vacancies(search_query, top_n)

    # Преобразование в список объектов
    vacancies = Vacancy.cast_to_object_list(vacancies_json)

    # Фильтрация по ключевому слову в описании
    if filter_word:
        vacancies = [vc for vc in vacancies if filter_word.lower() in vc.requirement.lower()]

    # Вывод на экран
    print_vacancies(vacancies)


if __name__ == "__main__":
    user_interaction()
