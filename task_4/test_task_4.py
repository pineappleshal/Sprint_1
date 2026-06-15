from task_4 import process_tasks


def test_next_task_returned():
    new_tasks = ['task_001', 'task_011', 'task_007', 'task_015', 'task_005']
    completed_tasks = ['task_002', 'task_012', 'task_006']

    result = process_tasks(new_tasks, completed_tasks)
    assert result == 'task_015'


def test_task_005_moved_to_completed():
    new_tasks = ['task_001', 'task_011', 'task_007', 'task_015', 'task_005']
    completed_tasks = ['task_002', 'task_012', 'task_006']

    process_tasks(new_tasks, completed_tasks)
    assert 'task_005' in completed_tasks
    assert 'task_005' not in new_tasks


def test_task_007_removed():
    new_tasks = ['task_001', 'task_011', 'task_007', 'task_015', 'task_005']
    completed_tasks = ['task_002', 'task_012', 'task_006']

    process_tasks(new_tasks, completed_tasks)
    assert 'task_007' not in new_tasks
    assert 'task_007' not in completed_tasks


def test_final_lists():
    new_tasks = ['task_001', 'task_011', 'task_007', 'task_015', 'task_005']
    completed_tasks = ['task_002', 'task_012', 'task_006']

    process_tasks(new_tasks, completed_tasks)
    assert new_tasks == ['task_001', 'task_011', 'task_015']
    assert completed_tasks == ['task_002', 'task_012', 'task_006', 'task_005']