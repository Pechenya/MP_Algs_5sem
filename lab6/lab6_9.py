def task9():
    m = int(input("Введите количество строк M: "))
    n = int(input("Введите количество столбцов N: "))
    a = input_matrix(m, n)
    if not a:
        print("Количество элементов в строке не совпадает с N")
    else:
        for i in range(m - 1):
            for j in range(m - 1 - i):
                if a[j][0] > a[j + 1][0]:
                    a[j], a[j + 1] = a[j + 1], a[j]
        print("Упорядоченная матрица:")
        print_matrix(a)

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
    task9()
