def task6():
    m = int(input("Введите количество строк M: "))
    n = int(input("Введите количество столбцов N: "))
    a = input_matrix(m, n)
    if not a:
        print("Количество элементов в строке не совпадает с N")
    else:
        for row in a:
            i_min = 0
            i_max = 0
            for j in range(n):
                if row[j] < row[i_min]:
                    i_min = j
                if row[j] > row[i_max]:
                    i_max = j
            row[i_min], row[i_max] = row[i_max], row[i_min]
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
    task6()
