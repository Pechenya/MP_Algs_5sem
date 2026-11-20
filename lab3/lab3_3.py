def task3():
    n = int(input("Введите целое число N (> 0): "))
    if n <= 0:
        print("Число N должно быть больше 0")
    else:
        s = 0
        for i in range(1, n + 1):
            s += 2 * i - 1
            print(f"Текущая сумма: {s}")
        print(f"Квадрат числа {n}: {s}")

if __name__ == '__main__':
    task3()
