def task8():
    n = int(input("Введите целое число: "))
    print(f"Количество цифр в числе: {digits(abs(n))}")

def digits(n):
    if n < 10:
        return 1
    else:
        return 1 + digits(n // 10)

if __name__ == '__main__':
    task8()
