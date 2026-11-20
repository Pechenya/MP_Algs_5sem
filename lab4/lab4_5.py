def task5():
    a = list(map(float, input("Введите элементы отсортированного массива через запятую с пробелом: ").split(', ')))
    x = float(input("Введите искомый элемент: "))
    sorted_flag = True
    for i in range(1, len(a)):
        if a[i] < a[i - 1]:
            sorted_flag = False
    if not sorted_flag:
        print("Массив должен быть отсортирован по возрастанию")
    else:
        index = binary_search(a, x, 0, len(a) - 1)
        if index == -1:
            print("Элемент не найден в массиве")
        else:
            print(f"Номер найденного элемента: {index + 1}")

def binary_search(a, x, left, right):
    if left > right:
        return -1
    middle = (left + right) // 2
    if a[middle] == x:
        return middle
    elif a[middle] < x:
        return binary_search(a, x, middle + 1, right)
    else:
        return binary_search(a, x, left, middle - 1)

if __name__ == '__main__':
    task5()
