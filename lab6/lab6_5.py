def task5():
    m = int(input("Введите количество строк M: "))
    n = int(input("Введите количество столбцов N: "))
    a = input_matrix(m, n)
    if not a:
        print("Количество элементов в строке не совпадает с N")
    else:
        number = 0
        for j in range(n):
            odd = True
            for i in range(m):
                if a[i][j] % 2 == 0:
                    odd = False
            if odd:
                number = j + 1
                break
        print(f"Номер первого столбца из нечетных чисел: {number}")

def input_matrix(m, n):
    a = []
    for i in range(m):
        row = list(map(int, input(f"Введите элементы {i + 1} строки через запятую с пробелом: ").split(', ')))
        if len(row) != n:
            return []
        a.append(row)
    return a

def print_matrix(a):
    for row in a:
        print(" ".join(map(str, row)))

if __name__ == '__main__':
    task5()
