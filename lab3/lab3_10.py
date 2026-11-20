def task10():
    a = int(input("Введите целое положительное число A: "))
    b = int(input("Введите целое положительное число B: "))
    if a <= 0 or b <= 0:
        print("Числа должны быть положительными")
    else:
        x, y = a, b
        while y != 0:
            x, y = y, x % y
        print(f"НОД({a}, {b}) = {x}")

if __name__ == '__main__':
    task10()
