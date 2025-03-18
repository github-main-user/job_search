from unittest.mock import MagicMock, patch

import pytest
from requests import HTTPError

from src.api import HeadHunterAPI


@pytest.fixture
def vacancies_json() -> list[dict]:
    return [
        {
            "name": "Developer",
            "salary": 100000,
            "url": "https://api.hh.ru/",
            "requirement": "Write code",
        },
        {
            "name": "Scientist",
            "salary": 200000,
            "url": "https://api.hh.ru/",
            "requirement": "Science",
        },
    ]


@patch("requests.get")
def test_get_vacancies_success(mock_get: MagicMock, vacancies_json: list[dict]) -> None:
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"items": vacancies_json}

    mock_get.return_value = mock_response

    hh = HeadHunterAPI()
    data = hh.get_vacancies("test")

    assert isinstance(data, list)
    assert len(data) == 2

    assert data[0]["name"] == "Developer"
    assert data[1]["name"] == "Scientist"


@patch("requests.get")
def test_get_vacancies_empty(mock_get: MagicMock, vacancies_json: list[dict]) -> None:
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {}

    mock_get.return_value = mock_response

    hh = HeadHunterAPI()
    data = hh.get_vacancies("test")

    assert isinstance(data, list)
    assert len(data) == 0


@patch("requests.get")
def test_get_vacancies_http_error(mock_get: MagicMock) -> None:
    mock_get.side_effect = HTTPError("HTTP error occured")

    hh = HeadHunterAPI()

    data = hh.get_vacancies("test")

    assert data == []
