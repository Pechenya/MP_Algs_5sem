def task2():
    n = int(input("Введите целое число N (> 0): "))
    if n <= 0:
        print("Число N должно быть больше 0")
    else:
        product = 1
        for i in range(1, n + 1):
            product *= 1 + i / 10
        print(f"Произведение: {product}")

if __name__ == '__main__':
    task2()
