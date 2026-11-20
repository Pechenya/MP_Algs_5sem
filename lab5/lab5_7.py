def task7():
    n = int(input("Введите размер массива N: "))
    a = list(map(int, input("Введите элементы массива через запятую с пробелом: ").split(', ')))
    if len(a) != n:
        print("Количество элементов не совпадает с N")
    elif n < 2:
        print("Массив должен содержать хотя бы 2 элемента")
    else:
        d = a[1] - a[0]
        for i in range(2, n):
            if a[i] - a[i - 1] != d:
                d = 0
                break
        print(f"Результат: {d}")

if __name__ == '__main__':
    task7()
