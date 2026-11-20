def task7():
    a = float(input("Введите положительное число A: "))
    b = float(input("Введите положительное число B (A > B): "))
    if a <= 0 or b <= 0 or a <= b:
        print("Числа должны быть положительными и A > B")
    else:
        rest = a
        while rest >= b:
            rest -= b
        print(f"Длина незанятой части отрезка A: {rest}")

if __name__ == '__main__':
    task7()
