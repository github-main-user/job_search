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
        self.__params = {"text": "", "per_page": 10}

    def _connect(self) -> dict | Any:
        """Загружает вакансии используя API hh.ru, возвращает полученный JSON."""
        response = requests.get(self.__url, headers=self.__headers, params=self.__params, timeout=5)
        response.raise_for_status()
        return response.json()

    def get_vacancies(self, keyword: str) -> list | Any:
        """
        Получает вакансии содержащие переданное ключевое слово, используя API hh.ru,
        возвращает список вакансий в формате JSON.
        """
        self.__params["text"] = keyword

        try:
            data = self._connect()
            return data.get("items", [])
        except requests.HTTPError:
            return []
