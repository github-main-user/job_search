from unittest.mock import MagicMock, mock_open, patch

import pytest

from src.file_handler import VacancyJsonHandler
from src.vacancy import Vacancy

# ==========
#  Fixtures
# ==========


@pytest.fixture
def correct_vacancy() -> Vacancy:
    return Vacancy("Name", "https://test.url.com", 100000, "Requirement")


# =======
#  Tests
# =======


@patch(
    "builtins.open",
    new_callable=mock_open,
    read_data='[{"name": "Vacancy1", "url": "https://url1.com", "salary": 10000, "requirements": "Requirements1"}]',
)
def test_load_vacancies(mock_file: MagicMock) -> None:
    vc_json_handler = VacancyJsonHandler()
    vacancies = vc_json_handler._load_vacancies()

    mock_file.assert_called()
    assert len(vacancies) == 1
    assert vacancies[0]["name"] == "Vacancy1"


@patch("builtins.open", new_callable=mock_open, read_data="wrong json")
def test_load_vacancies_wrong_json(mock_file: MagicMock) -> None:
    vc_json_handler = VacancyJsonHandler()
    vacancies = vc_json_handler._load_vacancies()

    mock_file.assert_called()
    assert len(vacancies) == 0


@patch("builtins.open", new_callable=mock_open)
def test_dump_vacancies(mock_file: MagicMock) -> None:
    vacancies = [
        {"name": "name", "url": "https://test.url.com", "salary": 120000, "requirement": "requirement"},
        {"name": "name2", "url": "https://test2.url.com", "salary": 130000, "requirement": "requirement2"},
    ]
    vc_json_handler = VacancyJsonHandler()
    vc_json_handler._dump_vacancies(vacancies)

    mock_file.assert_called_once()


@patch(
    "builtins.open",
    new_callable=mock_open,
    read_data='[{"name": "Vacancy1", "url": "https://url1.com", "salary": 10000, "requirements": "Requirements1"}]',
)
def test_add_vacancies(mock_file: MagicMock, correct_vacancy: Vacancy) -> None:
    vc_json_handler = VacancyJsonHandler()
    vc_json_handler.add_vacancy(correct_vacancy)

    mock_file.assert_called()


@patch("builtins.open", side_effect=FileNotFoundError)
def test_add_vacancies_file_not_found(mock_file: MagicMock, correct_vacancy: Vacancy) -> None:
    vc_json_handler = VacancyJsonHandler()
    with pytest.raises(FileNotFoundError):
        vc_json_handler.add_vacancy(correct_vacancy)


@patch("builtins.open", side_effect=FileNotFoundError)
def test_load_vacancies_file_not_found(mock_file: MagicMock) -> None:
    vc_json_handler = VacancyJsonHandler()
    with pytest.raises(FileNotFoundError):
        vc_json_handler._load_vacancies()


@patch(
    "builtins.open",
    new_callable=mock_open,
    read_data='[{"name": "Vacancy1", "url": "https://url1.com", "salary": 10000, "requirement": "Requirement1"}]',
)
def test_get_vacancy(mock_file: MagicMock) -> None:
    vc_json_handler = VacancyJsonHandler()
    vc = vc_json_handler.get_vacancy("vacan")

    assert vc is not None
    assert vc.name == "Vacancy1"


@patch(
    "builtins.open",
    new_callable=mock_open,
    read_data="[]",
)
def test_get_vacancy_empty(mock_file: MagicMock) -> None:
    vc_json_handler = VacancyJsonHandler()
    vc = vc_json_handler.get_vacancy("vacan")

    assert vc is None


@patch(
    "builtins.open",
    new_callable=mock_open,
    read_data='[{"name": "Vacancy1", "url": "https://url1.com", "salary": 10000, "requirements": "Requirements1"}]',
)
def test_delete_vacancy(mock_file: MagicMock) -> None:
    vc_json_handler = VacancyJsonHandler()
    vc_json_handler.delete_vacancy("vacan")

    mock_file.assert_called()
