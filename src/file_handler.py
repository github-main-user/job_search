from abc import ABC, abstractmethod

from .vacancy import Vacancy


class VacancyFileHandler(ABC):
    """Класс описывает методы для работы с файлом с вакансиями."""

    def __init__(self, file_name: str) -> None:
        pass

    @abstractmethod
    def save_vacancy(self, vacancy: Vacancy) -> None:
        """Добавляет вакансию в указанный при инициализации файл."""
        pass

    @abstractmethod
    def get_vacancy(self, pattern: str) -> Vacancy | None:
        """
        Возвращает вакансию из указанного при инициализации файла, содержащую переданную строку в имени.
        В случае отсутствия возвращает None.
        """
        pass

    @abstractmethod
    def delete_vacancy(self, pattern: str) -> None:
        """Удаляет вакансию из указанного при инициализации файла, содержащую переданную строку в имени."""
        pass
