def insertion_sort(arr):


def main():
    a = list(map(float, input("Введите массив через пробел: ").split(' ')))
    insertion_sort(a)
    print(a)

if __name__ == '__main__':
    main()