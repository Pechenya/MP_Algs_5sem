def task4():
    a = float(input("Введите вещественное число A: "))
    n = int(input("Введите целое число N (> 0): "))
    if n <= 0:
        print("Число N должно быть больше 0")
    else:
        s = 1
        power = 1
        for i in range(n):
            power *= a
            s += power
        print(f"Сумма: {s}")

if __name__ == '__main__':
    task4()
