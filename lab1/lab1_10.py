import math

def task10():
    x1, y1 = map(float, input("Введите координаты первой вершины (x1, y1): ").split(', '))
    x2, y2 = map(float, input("Введите координаты второй вершины (x2, y2): ").split(', '))
    x3, y3 = map(float, input("Введите координаты третьей вершины (x3, y3): ").split(', '))
    a = math.hypot(x2 - x1, y2 - y1)
    b = math.hypot(x3 - x2, y3 - y2)
    c = math.hypot(x1 - x3, y1 - y3)
    p = (a+b+c)/2
    print(f"Периметр: {a+b+c}")
    print(f"Площадь: {math.sqrt(p*(p-a)*(p-b)*(p-c))}")

if __name__ == '__main__':
    task10()