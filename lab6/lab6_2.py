def task2():
    m = int(input("Введите количество строк M: "))
    n = int(input("Введите количество столбцов N: "))
    a = input_matrix(m, n)
    if not a:
        print("Количество элементов в строке не совпадает с N")
    else:
        k = int(input("Введите номер строки K: "))
        if not 1 <= k <= m:
            print("Должно выполняться условие 1 ≤ K ≤ M")
        else:
            s = 0
            p = 1
            for x in a[k - 1]:
                s += x
                p *= x
            print(f"Сумма элементов {k} строки: {s}")
            print(f"Произведение элементов {k} строки: {p}")

def input_matrix(m, n):
    a = []
    for i in range(m):
        row = list(map(float, input(f"Введите элементы {i + 1} строки через запятую с пробелом: ").split(', ')))
        if len(row) != n:
            return []
        a.append(row)
    return a

def print_matrix(a):
    for row in a:
        print(" ".join(map(str, row)))

if __name__ == '__main__':
    task2()
