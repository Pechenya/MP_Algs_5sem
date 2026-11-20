def task1():
    m = int(input("Введите порядок матрицы M (нечетное число): "))
    if m <= 0 or m % 2 == 0:
        print("Порядок матрицы должен быть положительным нечетным числом")
        return
    a = input_matrix(m, m)
    if not a:
        print("Количество элементов в строке не совпадает с M")
    else:
        result = []
        for k in range(m // 2):
            last = m - 1 - k
            for i in range(k, last):
                result.append(a[i][k])
            for j in range(k, last):
                result.append(a[last][j])
            for i in range(last, k, -1):
                result.append(a[i][last])
            for j in range(last, k, -1):
                result.append(a[k][j])
        result.append(a[m // 2][m // 2])
        print(f"Элементы по спирали: {' '.join(map(str, result))}")

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
    task1()
