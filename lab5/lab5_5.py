def task5():
    n = int(input("Введите размер массива N: "))
    a = list(map(float, input("Введите элементы массива через запятую с пробелом: ").split(', ')))
    if len(a) != n:
        print("Количество элементов не совпадает с N")
    else:
        result = []
        for i in range(0, n, 2):
            result.append(a[i])
        last_even = n - 1 if n % 2 == 0 else n - 2
        for i in range(last_even, 0, -2):
            result.append(a[i])
        print(f"Элементы в заданном порядке: {result}")

if __name__ == '__main__':
    task5()
