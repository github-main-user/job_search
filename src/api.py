from abc import ABC, abstractmethod
from typing import Any

import requests


class APIParser(ABC):
    """Абстрактный класс, описывающий методы работы с API для поиска работы."""

    @abstractmethod
    def _connect(self, params: dict) -> dict:
        """Метод для получения данных с API."""
        pass

    @abstractmethod
    def get_vacancies(self, keyword: str, count: int) -> list:
        """Метод для получения списка вакансий, содержащих переданное ключевое слово."""
        pass


class HeadHunterAPI(APIParser):
    """Класс для работы с API HeadHunter"""

    def __init__(self) -> None:
        self.__url = "https://api.hh.ru/vacancies"
        self.__headers = {"User-Agent": "HH-User-Agent"}

    def _connect(self, params: dict) -> dict | Any:
        """Загружает вакансии используя API hh.ru, возвращает полученный JSON."""
        response = requests.get(self.__url, headers=self.__headers, params=params, timeout=5)
        response.raise_for_status()
        return response.json()

    def get_vacancies(self, keyword: str, count: int = 10) -> list | Any:
        """
        Получает вакансии содержащие переданное ключевое слово, используя API hh.ru,
        возвращает список вакансий в формате JSON.
        """

        try:
            data = self._connect(params={"text": keyword, "per_page": count})
            return data.get("items", [])
        except requests.HTTPError:
            return []
