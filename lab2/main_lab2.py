from lab2_1 import task1
from lab2_2 import task2
from lab2_3 import task3
from lab2_4 import task4
from lab2_5 import task5
from lab2_6 import task6
from lab2_7 import task7
from lab2_8 import task8
from lab2_9 import task9
from lab2_10 import task10

def task_choice():
    task = int(input("Введите задание для проверки или любое другое значение для выхода: "))
    match task:
        case 1:
            task1()
            return task_choice()
        case 2:
            task2()
            return task_choice()
        case 3:
            task3()
            return task_choice()
        case 4:
            task4()
            return task_choice()
        case 5:
            task5()
            return task_choice()
        case 6:
            task6()
            return task_choice()
        case 7:
            task7()
            return task_choice()
        case 8:
            task8()
            return task_choice()
        case 9:
            task9()
            return task_choice()
        case 10:
            task10()
            return task_choice()
        case _:
            print("Выход из режима проверки заданий")
            return 0

task_choice()