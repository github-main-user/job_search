import json
from abc import ABC, abstractmethod
from typing import Any

from .vacancy import Vacancy


class VacancyFileHandler(ABC):
    """Класс описывает методы для работы с файлом с вакансиями."""

    def __init__(self, file_name: str) -> None:
        pass

    @abstractmethod
    def add_vacancy(self, vacancy: Vacancy) -> None:
        """Добавляет вакансию в указанный при инициализации файл."""
        pass

    @abstractmethod
    def get_vacancy(self, pattern: str) -> Vacancy | None:
        """
        Возвращает вакансию из указанного при инициализации файла, содержащую переданную строку в названии.
        В случае отсутствия возвращает None.
        """
        pass

    @abstractmethod
    def delete_vacancy(self, pattern: str) -> None:
        """Удаляет вакансию из указанного при инициализации файла, содержащую переданную строку в названии."""
        pass


class VacancyJsonHandler(VacancyFileHandler):
    """Класс предостовляет методы для работы с вакансиями в JSON файле."""

    def __init__(self, file_name: str = "./data/vacancies.json") -> None:
        self.__file_name = file_name

    def _load_vacancies(self) -> list | Any:
        """Загружает ванаскии из файла, указанного при инициализации."""
        with open(self.__file_name, "r", encoding="utf-8") as file_obj:
            try:
                vacancies = json.load(file_obj)
            except json.JSONDecodeError:
                vacancies = []

        return vacancies

    def _dump_vacancies(self, vacancies: list[dict]) -> None:
        """Выгружает список транзакций в JSON файл, указанный при инициализации."""
        with open(self.__file_name, "w", encoding="utf-8") as file_obj:
            json.dump(vacancies, file_obj, ensure_ascii=False, indent=4)

    def add_vacancy(self, vacancy: Vacancy) -> None:
        """Добавляет вакансию в указанный при инициализации файл."""
        vacancies = self._load_vacancies()

        # Проверяет, есть ли уже вакансия с таким названием
        if not ([vc for vc in vacancies if vc.get("name") != vacancy.name]):
            vacancies.append(vacancy.to_dict())

        self._dump_vacancies(vacancies)

    def get_vacancy(self, pattern: str) -> Vacancy | None:
        """
        Возвращает вакансию из файла, указанного при инициализации,
        если она содержит переданную строку в названии.
        """
        vacancies = self._load_vacancies()

        for vc in vacancies:
            if pattern.lower() in vc.get("name", "").lower():
                return Vacancy(**vc)

        return None

    def delete_vacancy(self, pattern: str) -> None:
        """Удаляет вакансии, содержащие в названии переданную строку."""
        vacancies = self._load_vacancies()
        vacancies = [vc for vc in vacancies if vc.get("name", "").lower() != pattern.lower()]
        self._dump_vacancies(vacancies)
