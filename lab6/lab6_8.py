def task8():
    m = int(input("Введите количество строк M: "))
    n = int(input("Введите количество столбцов N: "))
    if m % 2 != 0 or n % 2 != 0:
        print("M и N должны быть четными числами")
        return
    a = input_matrix(m, n)
    if not a:
        print("Количество элементов в строке не совпадает с N")
    else:
        for i in range(m // 2):
            for j in range(n // 2):
                a[i][j], a[i + m // 2][j + n // 2] = a[i + m // 2][j + n // 2], a[i][j]
        print("Преобразованная матрица:")
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
    task8()
