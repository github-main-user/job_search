import pytest

from src.vacancy import Vacancy

# ==========
#  Fixtures
# ==========


@pytest.fixture
def correct_vacancy() -> Vacancy:
    return Vacancy(
        name="Name",
        salary=100000,
        url="https://test.url.com",
        requirement="Requirement",
    )


# =======
#  Tests
# =======


def test_init_values(correct_vacancy: Vacancy) -> None:
    assert correct_vacancy.name == "Name"
    assert correct_vacancy.salary == 100000
    assert correct_vacancy.url == "https://test.url.com"
    assert correct_vacancy.requirement == "Requirement"


def test_assign_non_slots_attribute(correct_vacancy: Vacancy) -> None:
    with pytest.raises(AttributeError):
        correct_vacancy.wrong_attr = 123  # type: ignore


def test_wrong_name_validation() -> None:
    with pytest.raises(ValueError):
        Vacancy(None, "https://test.url.com", 100000, "R")  # type: ignore

    with pytest.raises(ValueError):
        Vacancy(None, "https://test.url.com", 100000, "R")  # type: ignore


def test_wrong_url_validation() -> None:
    with pytest.raises(ValueError):
        Vacancy("N", "httpstesturlcom", 100000, "R")  # type: ignore

    with pytest.raises(ValueError):
        Vacancy("N", None, 100000, "R")  # type: ignore


def test_wrong_salary_validation() -> None:
    vc = Vacancy("N", "https://test.url.com", -100000, "R")  # type: ignore
    vc2 = Vacancy("N", "https://test.url.com", None, "R")  # type: ignore

    assert vc.salary == 0
    assert vc2.salary == 0


def test_wrong_requirement_validation() -> None:
    with pytest.raises(ValueError):
        Vacancy(None, "https://test.url.com", 100000, "")  # type: ignore

    with pytest.raises(ValueError):
        Vacancy(None, "https://test.url.com", 100000, None)  # type: ignore


def test_salary_comparison_wrong_type(correct_vacancy: Vacancy) -> None:
    with pytest.raises(TypeError):
        correct_vacancy == 2  # type: ignore

    with pytest.raises(TypeError):
        correct_vacancy != "UwU"  # type: ignore

    with pytest.raises(TypeError):
        correct_vacancy < ""  # type: ignore

    with pytest.raises(TypeError):
        correct_vacancy <= 0.5  # type: ignore

    with pytest.raises(TypeError):
        correct_vacancy > 2  # type: ignore

    with pytest.raises(TypeError):
        correct_vacancy >= 2  # type: ignore


def test_salary_correct_comparison(correct_vacancy: Vacancy) -> None:
    other_vacancy = Vacancy("T", "https://test.url.com", 120000, "R")

    # 100000 vs 120000
    assert (correct_vacancy == other_vacancy) is False
    assert (correct_vacancy != other_vacancy) is True
    assert (correct_vacancy < other_vacancy) is True
    assert (correct_vacancy <= other_vacancy) is True
    assert (correct_vacancy > other_vacancy) is False
    assert (correct_vacancy >= other_vacancy) is False
