from lab3_1 import task1
from lab3_2 import task2
from lab3_3 import task3
from lab3_4 import task4
from lab3_5 import task5
from lab3_6 import task6
from lab3_7 import task7
from lab3_8 import task8
from lab3_9 import task9
from lab3_10 import task10

def task_choice():
    task = int(input("Введите задание для проверки или любое другое число для выхода: "))
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