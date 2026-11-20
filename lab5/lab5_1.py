def task1():
    n = int(input("Введите целое число N (> 0): "))
    if n <= 0:
        print("Число N должно быть больше 0")
    else:
        a = []
        for i in range(n):
            a.append(2 * i + 1)
        print(f"Массив: {a}")

if __name__ == '__main__':
    task1()
