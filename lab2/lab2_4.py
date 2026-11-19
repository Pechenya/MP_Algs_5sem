def task4():
    x, y = map(float, input("Введите координаты точки (x, y): ").split(', '))
    if x == 0 or y == 0:
        print("Точка не должна лежать на координатных осях")
    elif x > 0 and y > 0:
        print("Точка находится в 1 четверти")
    elif x < 0 and y > 0:
        print("Точка находится во 2 четверти")
    elif x < 0 and y < 0:
        print("Точка находится в 3 четверти")
    else:
        print("Точка находится в 4 четверти")

if __name__ == '__main__':
    task4()
