import re
from typing import Self


class Vacancy:
    """Класс описывает вакансию, при инициализации валидирует аттрибуты."""

    __slots__ = ("name", "salary", "url", "requirement")

    def __init__(
        self,
        name: str,
        url: str,
        salary: int,
        requirement: str,
    ) -> None:
        self.name = self.__validate_name(name)
        self.url = self.__validate_url(url)
        self.salary = self.__validate_salary(salary)
        self.requirement = self.__validate_requirement(requirement)

    # VALIDATION
    @staticmethod
    def __validate_name(value: str) -> str:
        """Проверяет, является ли название вакансии непустой строкой."""
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Название вакансии должно быть непустой строкой.")
        return value.strip()

    @staticmethod
    def __validate_url(value: str) -> str:
        """Проверяет переданный URL на корректность с помощью regex."""
        url_pattern = re.compile(r"^(https?:\/\/)?([\w.-]+)\.([a-z]{2,6})(\/\S*)?$")
        if not isinstance(value, str) or not url_pattern.match(value):
            raise ValueError("Некорректный URL.")
        return value.strip()

    @staticmethod
    def __validate_salary(value: int) -> int:
        """Проверяет, указана ли зарплата, и является ли она положительным числом, иначе возвращает 0."""
        if not isinstance(value, int) or value < 0:
            return 0
        return value

    @staticmethod
    def __validate_requirement(value: str) -> str:
        """Проверяет, является ли поле "Требования" непустой строкой."""
        if not isinstance(value, str) or not value.strip():
            raise ValueError('Поле "Требования" должно быть непустой строкой.')
        clean_text = re.sub(r"</?highlighttext>", "", value)
        return clean_text.strip()

    # MAGIC METHODS

    def __str__(self) -> str:
        return f"""\
Вакансия: {self.name} ({"Зарплата: " + str(self.salary) if self.salary else "Зарплата не указана"})
Требования: {self.requirement}
Ссылка на вакансию: {self.url}"""

    # ==
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Vacancy):
            raise TypeError(f"Операция не поддерживается между {type(self)} и {type(other)}")
        return self.salary == other.salary

    # !=
    def __ne__(self, other: object) -> bool:
        return not self == other

    # <
    def __lt__(self, other: object) -> bool:
        if not isinstance(other, Vacancy):
            raise TypeError(f"Операция не поддерживается между {type(self)} и {type(other)}")
        return self.salary < other.salary

    # <=
    def __le__(self, other: object) -> bool:
        return self == other or self < other

    # >
    def __gt__(self, other: object) -> bool:
        return not self < other

    # >=
    def __ge__(self, other: object) -> bool:
        return not self <= other

    # GENERAL METHODS

    @classmethod
    def cast_to_object_list(cls, vacancies_json: list[dict]) -> list[Self]:
        """Преобразует список список словарей вакансий в список объектов этого класса."""
        return [
            cls(
                name=vacancy.get("name", ""),
                url=vacancy.get("url", ""),
                salary=(vacancy.get("salary") or {}).get("from", 0),
                requirement=vacancy.get("snippet", {}).get("requirement", ""),
            )
            for vacancy in vacancies_json
        ]

    def to_dict(self) -> dict:
        """Преобразует текущий экземпляр вакансии в словарь."""
        return {
            "name": self.name,
            "url": self.url,
            "salary": self.salary,
            "requirement": self.requirement,
        }
