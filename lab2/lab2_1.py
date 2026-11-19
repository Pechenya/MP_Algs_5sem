def task1():
    a = int(input("Введите целое число A: "))
    b = int(input("Введите целое число B: "))
    if a != b:
        a = b = max(a, b)
    else:
        a = b = 0
    print(f"A = {a}")
    print(f"B = {b}")

if __name__ == '__main__':
    task1()
