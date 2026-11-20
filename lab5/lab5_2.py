def task2():
    n = int(input("Введите целое число N (> 1): "))
    a = float(input("Введите первый член прогрессии A: "))
    d = float(input("Введите знаменатель прогрессии D: "))
    if n <= 1:
        print("Число N должно быть больше 1")
    else:
        arr = [a]
        for i in range(1, n):
            arr.append(arr[i - 1] * d)
        print(f"Массив: {arr}")

if __name__ == '__main__':
    task2()
