from task_3 import get_champions, check_country


def test_2022_added():
    champions = get_champions()
    assert champions[2022] == 'Аргентина'


def test_all_champions_present():
    champions = get_champions()
    assert len(champions) == 6
    assert champions[2002] == 'Бразилия'


def test_italy_was_champion():
    champions = get_champions()
    result = check_country(champions, 'Италия')
    assert result == 'Италия cтановилась чемпионом мира по футболу в 21 веке!'


def test_country_was_not_champion():
    champions = get_champions()
    result = check_country(champions, 'Россия')
    assert result == 'Россия не выигрывала чемпионат мира по футболу в 21 веке.'