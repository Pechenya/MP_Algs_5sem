def selection_sort(arr):
    for i in range(0, len(arr) - 1):
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[i]:
                arr[i], arr[j] = arr[j], arr[i]


def main():
    a = list(map(float, input("Введите массив через пробел: ").split(' ')))
    selection_sort(a)
    print(a)

if __name__ == '__main__':
    main()