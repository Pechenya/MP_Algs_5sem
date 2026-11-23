def insertion_sort(arr):
    for i in range(1, len(arr)):
        el = arr[i]
        j = i-1
        while j >= 0 and arr[j] > el:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = el


def main():
    a = list(map(float, input("Введите массив через пробел: ").split(' ')))
    insertion_sort(a)
    print(a)

if __name__ == '__main__':
    main()