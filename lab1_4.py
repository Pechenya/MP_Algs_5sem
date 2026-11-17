def task4():
    a = float(input("Введите ненулевое число a: "))
    b = float(input("Введите ненулевое число b: "))
    if a == 0 or b == 0:
        print("Числа должны быть ненулевыми")
    else:
        print(f"Сумма квадратов: {a*a + b*b}")
        print(f"Разность квадратов: {a*a - b*b}")
        print(f"Произведение квадратов: {a*a * b*b}")
        print(f"Частное квадратов: {a*a / b*b}")
if __name__ == '__main__':
    task4()