import math

def task3():
    xa, ya = map(float, input("Введите координаты точки A (x, y): ").split(', '))
    xb, yb = map(float, input("Введите координаты точки B (x, y): ").split(', '))
    xc, yc = map(float, input("Введите координаты точки C (x, y): ").split(', '))
    ab = math.hypot(xb - xa, yb - ya)
    ac = math.hypot(xc - xa, yc - ya)
    if ab < ac:
        print(f"Ближе к точке A расположена точка B ({xb}, {yb})")
        print(f"Расстояние от точки A до В: {ab}")
    elif ac < ab:
        print(f"Ближе к точке A расположена точка C ({xc}, {yc})")
        print(f"Расстояние от точки A до С: {ac}")
    else:
        print(f"Точки B и C расположены на одинаковом расстоянии от точки A: {ab}")

if __name__ == '__main__':
    task3()
