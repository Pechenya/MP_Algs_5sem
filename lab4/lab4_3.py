def task3():
    x = int(input("Введите число x: "))
    n = int(input("Введите степень n: "))
    if n > 0:
        print(power(x,n))
    elif n == 0:
        print(1)
    else:
        print(1/power(x,-n))

def power(x,n):
    if n == 1:
        return x
    else:
        return x*power(x,n-1)

if __name__ == '__main__':
    task3()
