def process_tasks(new_tasks, completed_tasks):
    # 1. Переносим task_005
    completed_tasks.append(new_tasks.pop(new_tasks.index('task_005')))

    # 2. Удаляем task_007
    new_tasks.remove('task_007')

    # 3. Возвращаем последнюю задачу
    return new_tasks[-1]


if __name__ == '__main__':
    new_tasks = ['task_001', 'task_011', 'task_007', 'task_015', 'task_005']
    completed_tasks = ['task_002', 'task_012', 'task_006']

    next_task = process_tasks(new_tasks, completed_tasks)
    print(next_task)