def task9():
    x1, y1 = map(float, input("Введите координаты первой вершины (x1, y1): ").split(', '))
    x2, y2 = map(float, input("Введите координаты второй вершины (x2, y2): ").split(', '))
    width = abs(x2 - x1)
    height = abs(y2 - y1)
    print(f"Периметр прямоугольника: {2 * (width + height)}")
    print(f"Площадь прямоугольника: {width * height}")

if __name__ == '__main__':
    task9()