def task3():
    n = int(input("Введите целое число N (> 2): "))
    a = int(input("Введите целое число A: "))
    b = int(input("Введите целое число B: "))
    if n <= 2:
        print("Число N должно быть больше 2")
    else:
        arr = [a, b]
        s = a + b
        for i in range(2, n):
            arr.append(s)
            s += arr[i]
        print(f"Массив: {arr}")

if __name__ == '__main__':
    task3()
