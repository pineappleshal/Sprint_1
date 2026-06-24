from task_5 import TestCase


def test_initial_state():
    test_case = TestCase()
    assert test_case.steps == {}
    assert test_case.result is None


def test_set_step_adds_step():
    test_case = TestCase()
    test_case.set_step(1, 'Перейти на сайт')
    assert test_case.steps == {1: 'Перейти на сайт'}


def test_set_step_multiple():
    test_case = TestCase()
    test_case.set_step(1, 'Шаг 1')
    test_case.set_step(2, 'Шаг 2')
    assert test_case.steps == {1: 'Шаг 1', 2: 'Шаг 2'}


def test_delete_step():
    test_case = TestCase()
    test_case.set_step(1, 'Шаг 1')
    test_case.set_step(2, 'Шаг 2')
    test_case.delete_step(1)
    assert test_case.steps == {2: 'Шаг 2'}


def test_set_step_overwrites_existing():
    test_case = TestCase()
    test_case.set_step(1, 'Старый текст')
    test_case.set_step(1, 'Новый текст')
    assert test_case.steps == {1: 'Новый текст'}


def test_set_result():
    test_case = TestCase()
    test_case.set_result('Товар в корзине')
    assert test_case.result == 'Товар в корзине'


def test_get_test_case_output(capsys):
    test_case = TestCase()
    test_case.set_step(1, 'Перейти на сайт')
    test_case.set_result('Сайт открыт')
    test_case.get_test_case()

    captured = capsys.readouterr()
    assert captured.out.strip() == "{'Шаги': {1: 'Перейти на сайт'}, 'Ожидаемый результат': 'Сайт открыт'}"


def test_two_instances_independent():
    test_case_1 = TestCase()
    test_case_2 = TestCase()
    test_case_1.set_step(1, 'Шаг для первого')
    assert test_case_2.steps == {}