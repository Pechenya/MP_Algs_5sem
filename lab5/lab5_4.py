def task4():
    n = int(input("Введите размер массива N: "))
    a = list(map(float, input("Введите элементы массива через запятую с пробелом: ").split(', ')))
    if len(a) != n:
        print("Количество элементов не совпадает с N")
    else:
        result = []
        for i in range(n // 2):
            result.append(a[i])
            result.append(a[n - 1 - i])
        if n % 2 == 1:
            result.append(a[n // 2])
        print(f"Элементы в заданном порядке: {result}")

if __name__ == '__main__':
    task4()
