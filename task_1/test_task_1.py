from task_1 import calculate_minutes


def test_calculate_minutes():
    assert calculate_minutes('1h 45m,360s,25m,30m 120s,2h 60s') == 289