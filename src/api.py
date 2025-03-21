from abc import ABC, abstractmethod
from typing import Any

import requests


class APIParser(ABC):
    """Абстрактный класс, описывающий методы работы с API для поиска работы."""

    @abstractmethod
    def _connect(self) -> dict:
        """Метод для получения данных с API."""
        pass

    @abstractmethod
    def get_vacancies(self, keyword: str) -> list:
        """Метод для получения списка вакансий, содержащих переданное ключевое слово."""
        pass


class HeadHunterAPI(APIParser):
    """Класс для работы с API HeadHunter"""

    def __init__(self) -> None:
        self.__url = "https://api.hh.ru/vacancies"
        self.__headers = {"User-Agent": "HH-User-Agent"}
        self.__params: dict = {"per_page": 100}

    def _connect(self) -> dict | Any:
        """Загружает вакансии используя API hh.ru, возвращает полученный JSON."""
        try:
            response = requests.get(self.__url, headers=self.__headers, params=self.__params, timeout=5)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException:
            return {}

    def get_vacancies(self, keyword: str) -> list[dict[str, Any]]:
        """
        Получает вакансии содержащие переданное ключевое слово, используя API hh.ru,
        возвращает список вакансий в формате словаря.
        """
        if not keyword.strip():
            return []

        self.__params["text"] = keyword.strip()

        vacancies = []
        for page_num in range(20):
            self.__params["page"] = page_num
            data = self._connect()

            # Либо закончились страницы, либо случилась ошибка
            if "items" not in data:
                break

            vacancies.extend(data["items"])

        return vacancies
