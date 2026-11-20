def task8():
    n = int(input("Введите размер массива N: "))
    a = list(map(float, input("Введите элементы массива через запятую с пробелом: ").split(', ')))
    if len(a) != n:
        print("Количество элементов не совпадает с N")
    elif n < 2:
        print("В массиве нет элементов с четными номерами")
    else:
        minimum = a[1]
        for i in range(3, n, 2):
            if a[i] < minimum:
                minimum = a[i]
        print(f"Минимальный элемент с четным номером: {minimum}")

if __name__ == '__main__':
    task8()
