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


@pytest.fixture
def vacancies_json() -> list[dict]:
    return [
        {
            "id": "93353083",
            "premium": False,
            "name": "Тестировщик комфорта квартир",
            "department": None,
            "has_test": False,
            "response_letter_required": False,
            "area": {"id": "26", "name": "Воронеж", "url": "https://api.hh.ru/areas/26"},
            "salary": {"from": 350000, "to": 450000, "currency": "RUR", "gross": False},
            "type": {"id": "open", "name": "Открытая"},
            "address": None,
            "response_url": None,
            "sort_point_distance": None,
            "published_at": "2024-02-16T14:58:28+0300",
            "created_at": "2024-02-16T14:58:28+0300",
            "archived": False,
            "apply_alternate_url": "https://hh.ru/applicant/vacancy_response?vacancyId=93353083",
            "branding": {"type": "CONSTRUCTOR", "tariff": "BASIC"},
            "show_logo_in_search": True,
            "insider_interview": None,
            "url": "https://api.hh.ru/vacancies/93353083?host=hh.ru",
            "alternate_url": "https://hh.ru/vacancy/93353083",
            "relations": [],
            "employer": {
                "id": "3499705",
                "name": "Специализированный застройщик BM GROUP",
                "url": "https://api.hh.ru/employers/3499705",
                "alternate_url": "https://hh.ru/employer/3499705",
                "logo_urls": {
                    "original": "https://hhcdn.ru/employer-logo-original/1214854.png",
                    "240": "https://hhcdn.ru/employer-logo/6479866.png",
                    "90": "https://hhcdn.ru/employer-logo/6479865.png",
                },
                "vacancies_url": "https://api.hh.ru/vacancies?employer_id=3499705",
                "accredited_it_employer": False,
                "trusted": True,
            },
            "snippet": {
                "requirement": "Занимать активную жизненную позицию, уметь активно танцевать и громко петь. "
                "Обладать навыками коммуникации, чтобы налаживать добрососедские отношения. "
                "Обладать системным мышлением...",
                "responsibility": "Оценивать вид из окна: встречать рассветы на кухне,"
                " и провожать алые закаты в спальне. "
                "Оценивать инфраструктуру района: ежедневно ходить на...",
            },
            "contacts": None,
            "schedule": {"id": "flexible", "name": "Гибкий график"},
            "working_days": [],
            "working_time_intervals": [],
            "working_time_modes": [],
            "accept_temporary": False,
            "professional_roles": [{"id": "107", "name": "Руководитель проектов"}],
            "accept_incomplete_resumes": False,
            "experience": {"id": "noExperience", "name": "Нет опыта"},
            "employment": {"id": "full", "name": "Полная занятость"},
            "adv_response_url": None,
            "is_adv_vacancy": False,
            "adv_context": None,
        },
        {
            "id": "92223756",
            "premium": False,
            "name": "Удаленный диспетчер чатов (в Яндекс)",
            "department": None,
            "has_test": False,
            "response_letter_required": False,
            "area": {"id": "113", "name": "Россия", "url": "https://api.hh.ru/areas/113"},
            "salary": {"from": 30000, "to": 44000, "currency": "RUR", "gross": True},
            "type": {"id": "open", "name": "Открытая"},
            "address": None,
            "response_url": None,
            "sort_point_distance": None,
            "published_at": "2024-01-25T17:37:04+0300",
            "created_at": "2024-01-25T17:37:04+0300",
            "archived": False,
            "apply_alternate_url": "https://hh.ru/applicant/vacancy_response?vacancyId=92223756",
            "show_logo_in_search": None,
            "insider_interview": None,
            "url": "https://api.hh.ru/vacancies/92223756?host=hh.ru",
            "alternate_url": "https://hh.ru/vacancy/92223756",
            "relations": [],
            "employer": {
                "id": "9498120",
                "name": "Яндекс Команда для бизнеса",
                "url": "https://api.hh.ru/employers/9498120",
                "alternate_url": "https://hh.ru/employer/9498120",
                "logo_urls": {
                    "original": "https://hhcdn.ru/employer-logo-original/1121425.jpg",
                    "90": "https://hhcdn.ru/employer-logo/6106293.jpeg",
                    "240": "https://hhcdn.ru/employer-logo/6106294.jpeg",
                },
                "vacancies_url": "https://api.hh.ru/vacancies?employer_id=9498120",
                "accredited_it_employer": False,
                "trusted": True,
            },
            "snippet": {
                "requirement": "Способен работать в команде. Способен принимать решения самостоятельно."
                " Готов учиться и узнавать новое. Опыт работы в колл-центре или службе...",
                "responsibility": "Работать с клиентами или партнерами для решения разнообразных ситуаций. "
                "Совершать звонки по их обращениям и давать письменные ответы. ",
            },
            "contacts": None,
            "schedule": {"id": "remote", "name": "Удаленная работа"},
            "working_days": [],
            "working_time_intervals": [],
            "working_time_modes": [{"id": "start_after_sixteen", "name": "Можно начинать работать после 16:00"}],
            "accept_temporary": False,
            "professional_roles": [{"id": "40", "name": "Другое"}],
            "accept_incomplete_resumes": True,
            "experience": {"id": "noExperience", "name": "Нет опыта"},
            "employment": {"id": "full", "name": "Полная занятость"},
            "adv_response_url": None,
            "is_adv_vacancy": False,
            "adv_context": None,
        },
    ]


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


def test_cast_to_object_list(vacancies_json: list[dict]) -> None:
    vc1, vc2 = Vacancy.cast_to_object_list(vacancies_json)

    assert vc1.name == "Тестировщик комфорта квартир"
    assert vc1.salary == 350000
    assert vc1.url == "https://api.hh.ru/vacancies/93353083?host=hh.ru"
    assert (
        vc1.requirement == "Занимать активную жизненную позицию, уметь активно танцевать и громко петь."
        " Обладать навыками коммуникации, чтобы налаживать добрососедские отношения."
        " Обладать системным мышлением..."
    )

    assert vc2.name == "Удаленный диспетчер чатов (в Яндекс)"
    assert vc2.salary == 30000
    assert vc2.url == "https://api.hh.ru/vacancies/92223756?host=hh.ru"
    assert (
        vc2.requirement == "Способен работать в команде. Способен принимать решения самостоятельно."
        " Готов учиться и узнавать новое. Опыт работы в колл-центре или службе..."
    )


def test_vacancy_to_dict_cast(correct_vacancy: Vacancy) -> None:
    vc_dict = correct_vacancy.to_dict()

    assert correct_vacancy.name == vc_dict["name"]
    assert correct_vacancy.url == vc_dict["url"]
    assert correct_vacancy.salary == vc_dict["salary"]
    assert correct_vacancy.requirement == vc_dict["requirement"]
