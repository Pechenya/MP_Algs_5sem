def bubble_sort(arr):
    for i in range(0, len(arr) - 1):
        swapped = False
        for j in range(0, len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if swapped == False:
            break


def main():
    a = list(map(float, input("Введите массив через пробел: ").split(' ')))
    bubble_sort(a)
    print(a)

if __name__ == '__main__':
    main()