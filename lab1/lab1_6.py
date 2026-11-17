import math
def task6():
    x1, y1 = map(float, input("Введите координаты первой точки (x1, y1): ").split(', '))
    x2, y2 =  map(float, input("Введите координаты второй точки (x2, y2): ").split(', '))
    print(f"Расстояние: {math.hypot(x2 - x1, y2 - y1)}")

if __name__ == '__main__':
    task6()