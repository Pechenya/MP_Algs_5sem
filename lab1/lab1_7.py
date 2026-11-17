def task7():
    a = float(input("Введите число a: "))
    b = float(input("Введите число b: "))
    c = float(input("Введите число c: "))
    print(f"Длина отрезка AC: {abs(c-a)}")
    print(f"Длина отрезка BC: {abs(c-b)}")
    print(f"Сумма длин отрезков AC и BC: {abs(c-a) + abs(c-b)}")

if __name__ == '__main__':
    task7()