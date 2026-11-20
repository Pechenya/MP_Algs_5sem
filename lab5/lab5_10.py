def task10():
    n = int(input("Введите размер массива N: "))
    a = list(map(int, input("Введите элементы массива через запятую с пробелом: ").split(', ')))
    if len(a) != n:
        print("Количество элементов не совпадает с N")
    else:
        first = second = 0
        for i in range(n):
            for j in range(i + 1, n):
                if a[i] == a[j]:
                    first = i + 1
                    second = j + 1
        if first == 0:
            print("В массиве нет одинаковых элементов")
        else:
            print(f"Номера одинаковых элементов: {first} {second}")

if __name__ == '__main__':
    task10()
