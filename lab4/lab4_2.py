def task2():
    n = int(input("Введите n для поиска элемента ряда Фибоначчи: "))
    if n > 0:
        print(fibon(n))
    else:
        print("Возможно найти число Фибоначчи только для целого положительного числа")

def fibon(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibon(n - 1) + fibon(n - 2)

if __name__ == '__main__':
    task2()
