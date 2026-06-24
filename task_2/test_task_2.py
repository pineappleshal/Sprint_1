from task_2 import Tester


def test_tester_with_deadline(capsys):
    tester = Tester('tester_2')
    tester.work_hard()
    captured = capsys.readouterr()
    assert captured.out.strip() == 'tester_2 Что ж, ещё часок поработаю!'


def test_tester_without_deadline(capsys):
    tester = Tester('tester_1')
    tester.deadline = False
    tester.work_hard()
    captured = capsys.readouterr()
    assert captured.out.strip() == 'tester_1 Можно отдыхать'