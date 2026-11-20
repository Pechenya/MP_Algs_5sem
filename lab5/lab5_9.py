def task9():
    n = int(input("Введите размер массива N: "))
    a = list(map(float, input("Введите элементы массива через запятую с пробелом: ").split(', ')))
    if len(a) != n:
        print("Количество элементов не совпадает с N")
    elif n < 2:
        print("Массив должен содержать хотя бы 2 элемента")
    else:
        number = 0
        for i in range(n):
            left = i == 0 or a[i] > a[i - 1]
            right = i == n - 1 or a[i] > a[i + 1]
            if left and right:
                number = i + 1
        if number == 0:
            print("В массиве нет локальных максимумов")
        else:
            print(f"Номер последнего локального максимума: {number}")

if __name__ == '__main__':
    task9()
