def task6():
    a = int(input("Введите целое положительное число A: "))
    b = int(input("Введите целое положительное число B (A < B): "))
    if a <= 0 or b <= 0 or a >= b:
        print("Числа должны быть положительными и A < B")
    else:
        for i in range(a, b + 1):
            for j in range(i):
                print(i, end=" ")
            print()

if __name__ == '__main__':
    task6()
