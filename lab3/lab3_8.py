def task8():
    n = int(input("Введите целое число N (> 1): "))
    if n <= 1:
        print("Число N должно быть больше 1")
    else:
        k = 0
        s = 0
        while s < n:
            k += 1
            s += k
        print(f"K = {k}")
        print(f"Сумма = {s}")

if __name__ == '__main__':
    task8()
