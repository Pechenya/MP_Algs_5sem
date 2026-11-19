def task6():
    n = int(input("Введите целое число от 1 до 999: "))
    if n < 1 or n > 999:
        print("Число должно лежать в диапазоне 1-999")
    else:
        parity = "четное" if n % 2 == 0 else "нечетное"
        if n < 10:
            digits = "однозначное"
        elif n < 100:
            digits = "двузначное"
        else:
            digits = "трехзначное"
        print(f"{parity} {digits} число")

if __name__ == '__main__':
    task6()
