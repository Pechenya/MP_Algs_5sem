def task6():
    n = int(input("Введите размер массива N: "))
    a = list(map(float, input("Введите элементы массива через запятую с пробелом: ").split(', ')))
    k = int(input("Введите номер K: "))
    l = int(input("Введите номер L: "))
    if len(a) != n:
        print("Количество элементов не совпадает с N")
    elif not 1 <= k <= l <= n:
        print("Должно выполняться условие 1 ≤ K ≤ L ≤ N")
    else:
        s = 0
        for i in range(k - 1, l):
            s += a[i]
        print(f"Среднее арифметическое элементов с номерами от {k} до {l}: {s / (l - k + 1)}")

if __name__ == '__main__':
    task6()
