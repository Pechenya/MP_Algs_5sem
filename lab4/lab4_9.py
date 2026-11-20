def task9():
    n = int(input("Введите количество дисков: "))
    if n > 0:
        hanoi(n, "A", "B", "C")
    else:
        print("Количество дисков должно быть целым положительным числом")

def hanoi(n, source, target, auxiliary):
    if n == 1:
        print(f"Переместить диск 1 со стержня {source} на стержень {target}")
        return
    hanoi(n - 1, source, auxiliary, target)
    print(f"Переместить диск {n} со стержня {source} на стержень {target}")
    hanoi(n - 1, auxiliary, target, source)

if __name__ == '__main__':
    task9()
