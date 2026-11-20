def task4():
    m = int(input("Введите количество строк M: "))
    n = int(input("Введите количество столбцов N: "))
    a = input_matrix(m, n)
    if not a:
        print("Количество элементов в строке не совпадает с N")
    else:
        for j in range(n):
            s = 0
            for i in range(m):
                s += a[i][j]
            average = s / m
            count = 0
            for i in range(m):
                if a[i][j] > average:
                    count += 1
            print(f"Столбец {j + 1}: {count}")

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
    task4()
