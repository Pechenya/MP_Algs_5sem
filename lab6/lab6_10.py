def task10():
    m = int(input("Введите порядок матрицы M: "))
    a = input_matrix(m, m)
    if not a:
        print("Количество элементов в строке не совпадает с M")
    else:
        for d in range(m - 1, -m, -1):
            s = 0
            for i in range(m):
                j = i - d
                if 0 <= j < m:
                    s += a[i][j]
            print(f"Сумма диагонали i - j = {d}: {s}")

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
    task10()
