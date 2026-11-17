def task5():
    a = float(input("Введите ненулевое число a: "))
    b = float(input("Введите ненулевое число b: "))
    if a == 0 or b == 0:
        print("Числа должны быть ненулевыми")
    else:
        print(f"Сумма квадратов: {abs(a) + abs(b)}")
        print(f"Разность квадратов: {abs(a) - abs(b)}")
        print(f"Произведение квадратов: {abs(a) * abs(b)}")
        print(f"Частное квадратов: {abs(a) / abs(b)}")
if __name__ == '__main__':
    task5()