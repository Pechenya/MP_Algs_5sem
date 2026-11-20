def task9():
    p = float(input("Введите процент P (0 < P < 25): "))
    if p <= 0 or p >= 25:
        print("Процент P должен лежать в диапазоне 0 < P < 25")
    else:
        s = 1000
        k = 0
        while s <= 1100:
            s += s * p / 100
            k += 1
        print(f"Количество месяцев (K): {k}")
        print(f"Итоговый размер вклада (S): {s}")

if __name__ == '__main__':
    task9()
