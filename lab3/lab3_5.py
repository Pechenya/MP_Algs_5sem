def task5():
    a = float(input("Введите вещественное число A: "))
    n = int(input("Введите целое число N (> 0): "))
    if n > 0 :
        s = 1
        term = 1
        for i in range(n):
            term *= -a
            s += term
        print(f"Значение выражения: {s}")
    else:
        print(f"Число N должно быть больше 0, введенное число N={n}.")

if __name__ == '__main__':
    task5()
