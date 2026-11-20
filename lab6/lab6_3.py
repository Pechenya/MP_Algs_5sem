def task3():
    m = int(input("Введите количество строк M: "))
    n = int(input("Введите количество столбцов N: "))
    a = input_matrix(m, n)
    if not a:
        print("Количество элементов в строке не совпадает с N")
    else:
        number = 0
        minimum = 0
        for j in range(n):
            p = 1
            for i in range(m):
                p *= a[i][j]
            if j == 0 or p < minimum:
                minimum = p
                number = j + 1
        print(f"Номер столбца с наименьшим произведением: {number}")
        print(f"Наименьшее произведение: {minimum}")

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
    task3()
