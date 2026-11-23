from m1_Sort.lab7_Bubble_sort import bubble_sort


def binary_search(arr, search):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == search:
            return True
        elif arr[mid] < search:
            low = mid + 1
        else:
            high = mid - 1
    return False


def main():
    a = list(map(float, input("Введите массив через пробел: ").split(' ')))
    b = float(input("Введите элемент поиска: "))
    bubble_sort(a)
    if binary_search(a, b):
        print("Элемент в списке")
    else:
        print("Такого элемента нет")

if __name__ == '__main__':
    main()