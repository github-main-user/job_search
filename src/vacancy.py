class Vacancy:
    """Класс описывает вакансию, при инициализации валидирует аттрибуты."""

    __slots__ = ("name", "area_name", "salary", "url", "requirement")

    def __init__(
        self,
        name: str,
        area_name: str,
        salary: int,
        url: str,
        requirement: str,
    ) -> None:
        self.name = self.__validate_str(name, "Название вакансии")
        self.area_name = self.__validate_str(area_name, "Город вакансии")
        self.salary = self.__validate_salary(salary)
        self.url = self.__validate_url(url)
        self.requirement = self.__validate_str(requirement, "Требования")

    # VALIDATION
    @staticmethod
    def __validate_str(value: str, field_name: str) -> str:
        """Проверяет, является ли переданный объект непустой строкой."""
        if not isinstance(value, str) or not value.strip():
            raise ValueError(f"Поле {field_name} должно быть непустой строкой.")
        return value.strip()

    @staticmethod
    def __validate_salary(value: int) -> int:
        """Проверяет, указана ли зарплата, и является ли она положительным числом"""
        if not isinstance(value, int) or value < 0:
            raise ValueError("Зарплата должна быть положительным числом.")
        return value

    @staticmethod
    def __validate_url(value: str) -> str:
        """Проверяет переданный URL на корректность с помощью regex."""
        import re

        url_pattern = re.compile(r"^(https?:\/\/)?([\w.-]+)\.([a-z]{2,6}\.?)(\/[\w.-]*)*\/?$")
        if not isinstance(value, str) or not url_pattern.match(value):
            raise ValueError("Некорректный URL.")
        return value.strip()

    # MAGIC METHODS FOR COMPARISON

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
