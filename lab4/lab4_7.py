def task7():
    n = int(input("Введите целое число n (> 1): "))
    if n > 1:
        print(f"{n} = {' + '.join(map(str, prime_sum(n)))}")
    else:
        print("Разложить на сумму простых чисел возможно только число больше 1")

#Проверяем простое ли число - нет ли делителей (в рекурсии)
def is_prime(n, d=2):
    if n < 2:
        return False
    elif d * d > n:
        return True
    elif n % d == 0:
        return False
    else:
        return is_prime(n, d + 1)

#Ищем ближайшее простое число, которое равно или меньше n
def prev_prime(n):
    if is_prime(n):
        return n
    else:
        return prev_prime(n - 1)

#Раскладываем наибольшее простое и его остаток в рекурсии. Берем 2, чтобы не получить 1
def prime_sum(n):
    if is_prime(n):
        return [n]
    p = prev_prime(n - 2)
    return [p] + prime_sum(n - p)

if __name__ == '__main__':
    task7()
