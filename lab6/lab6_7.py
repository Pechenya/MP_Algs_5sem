def task7():
    m = int(input("Введите количество строк M: "))
    n = int(input("Введите количество столбцов N: "))
    a = input_matrix(m, n)
    if not a:
        print("Количество элементов в строке не совпадает с N")
    else:
        i_min, j_min = 0, 0
        i_max, j_max = 0, 0
        for i in range(m):
            for j in range(n):
                if a[i][j] < a[i_min][j_min]:
                    i_min, j_min = i, j
                if a[i][j] > a[i_max][j_max]:
                    i_max, j_max = i, j
        for i in range(m):
            a[i][j_min], a[i][j_max] = a[i][j_max], a[i][j_min]
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
    task7()
