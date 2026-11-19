def task2():
    a = float(input("Введите число a: "))
    b = float(input("Введите число b: "))
    c = float(input("Введите число c: "))
    print(f"Сумма двух наибольших чисел: {a + b + c - min(a, b, c)}")

if __name__ == '__main__':
    task2()
