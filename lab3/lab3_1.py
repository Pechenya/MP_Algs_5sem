def task1():
    price = float(input("Введите цену 1 кг конфет: "))
    for i in range(1, 11):
        weight = i / 10
        print(f"Стоимость {weight} кг конфет: {price * weight}")

if __name__ == '__main__':
    task1()
