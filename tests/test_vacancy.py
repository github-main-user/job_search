import pytest

from src.vacancy import Vacancy

# ==========
#  Fixtures
# ==========


@pytest.fixture
def correct_vacancy() -> Vacancy:
    return Vacancy(
        name="Name",
        area_name="Area Name",
        salary=100000,
        url="https://test.url.com",
        requirement="Requirement",
    )


# =======
#  Tests
# =======


def test_init_values(correct_vacancy: Vacancy) -> None:
    assert correct_vacancy.name == "Name"
    assert correct_vacancy.area_name == "Area Name"
    assert correct_vacancy.salary == 100000
    assert correct_vacancy.url == "https://test.url.com"
    assert correct_vacancy.requirement == "Requirement"


def test_assign_non_slots_attribute(correct_vacancy: Vacancy) -> None:
    with pytest.raises(AttributeError):
        correct_vacancy.wrong_attr = 123  # type: ignore


def test_wrong_str_validation() -> None:
    with pytest.raises(ValueError):
        Vacancy("", "", 100000, "https://test.url.com", "")

    with pytest.raises(ValueError):
        Vacancy(None, None, 100000, "https://test.url.com", None)  # type: ignore


def test_wrong_salary_validation() -> None:
    with pytest.raises(ValueError):
        Vacancy("Name", "Area Name", None, "https://test.url.com", "Requirement")  # type: ignore

    with pytest.raises(ValueError):
        Vacancy("Name", "Area Name", -50, "https://test.url.com", "Requirement")  # type: ignore


def test_wrong_url_validation() -> None:
    with pytest.raises(ValueError):
        Vacancy("Name", "Area Name", 100000, "httpstesturlcom", "Requirement")  # type: ignore

    with pytest.raises(ValueError):
        Vacancy("Name", "Area Name", 100000, None, "Requirement")  # type: ignore


def test_salary_comparison_wrong_type(correct_vacancy: Vacancy) -> None:
    with pytest.raises(TypeError):
        correct_vacancy == 2  # type: ignore

    with pytest.raises(TypeError):
        correct_vacancy is not None  # type: ignore

    with pytest.raises(TypeError):
        correct_vacancy < ""  # type: ignore

    with pytest.raises(TypeError):
        correct_vacancy <= 0.5  # type: ignore

    with pytest.raises(TypeError):
        correct_vacancy > 2  # type: ignore

    with pytest.raises(TypeError):
        correct_vacancy >= 2  # type: ignore


def test_salary_correct_comparison(correct_vacancy: Vacancy) -> None:
    other_vacancy = Vacancy("T", "A", 120000, "https://test.url.com", "R")

    # 100000 vs 120000
    assert (correct_vacancy == other_vacancy) is False
    assert (correct_vacancy != other_vacancy) is True
    assert (correct_vacancy < other_vacancy) is True
    assert (correct_vacancy <= other_vacancy) is True
    assert (correct_vacancy > other_vacancy) is False
    assert (correct_vacancy >= other_vacancy) is False
