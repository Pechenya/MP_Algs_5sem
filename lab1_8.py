def task8():
    a = float(input("Введите число a: "))
    b = float(input("Введите число b: "))
    c = float(input("Введите число c: "))
    print(f"Произведение длин отрезков AC и BC: {abs(c - a) * abs(c - b)}")

if __name__ == '__main__':
    task8()