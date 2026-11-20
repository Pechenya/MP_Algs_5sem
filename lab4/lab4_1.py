def task1():
    n = int(input("Введите целое число n для поиска факториала: "))
    if n > 0:
        print(factorial(n))
    else:
        print("Возможно вычислить факториал только для целого положительного числа")

def factorial(n):
    if n > 1:
        return n*factorial(n-1)
    elif n == 1:
        return 1

if __name__ == '__main__':
    task1()
