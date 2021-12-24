def show_main_menu():
    print('----------------------------------------------------------')
    number = int(input('Введите номер задачи : '))
    if 1 <= number <= 16:
        __go_to_task(number)
    else:
        print('Неверный номер, повторите')
        show_main_menu()


def __go_to_task(number: int):
    if number == 1:
        from task1 import Task1
        task = Task1(task_ended_callback)
        task.start_task()
    elif number == 2:
        from task2 import Task2
        task = Task2(task_ended_callback)
        task.start_task()
    elif number == 3:
        from task3 import Task3
        task = Task3(task_ended_callback)
        task.start_task()
    elif number == 4:
        from task4 import Task4
        task = Task4(task_ended_callback)
        task.start_task()
    elif number == 5:
        from task5 import Task5
        task = Task5(task_ended_callback)
        task.start_task()
    elif number == 6:
        from task6 import Task6
        task = Task6(task_ended_callback)
        task.start_task()
    elif number == 7:
        from task7 import Task7
        task = Task7(task_ended_callback)
        task.start_task()
    elif number == 8:
        from task8 import Task8
        task = Task8(task_ended_callback)
        task.start_task()
    elif number == 9:
        from task9 import Task9
        task = Task9(task_ended_callback)
        task.start_task()
    elif number == 10:
        from task10 import Task10
        task = Task10(task_ended_callback)
        task.start_task()
    elif number == 11:
        from task11 import Task11
        task = Task11(task_ended_callback)
        task.start_task()
    elif number == 12:
        from task12 import Task12
        task = Task12(task_ended_callback)
        task.start_task()
    elif number == 13:
        from task13 import Task13
        task = Task13(task_ended_callback)
        task.start_task()
    elif number == 14:
        from task14 import Task14
        task = Task14(task_ended_callback)
        task.start_task()
    elif number == 15:
        from task15 import Task15
        task = Task15(task_ended_callback)
        task.start_task()
    elif number == 16:
        from task16 import Task16
        task = Task16(task_ended_callback)
        task.start_task()
    else:
        print('Неверный номер, повторите')
        show_main_menu()


def task_ended_callback(number: int):
    a = float(input('Назад к задачам(1), повторить задачу(2): '))
    if a == 1:
        show_main_menu()
    elif a == 2:
        __go_to_task(number)
    else:
        print('Неверный номер, повторите')
        task_ended_callback(number)


show_main_menu()