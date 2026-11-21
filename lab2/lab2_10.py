def task10():
    year = int(input("Введите номер года: "))
    colors_f = ["зеленой", "красной", "желтой", "белой", "черной"]
    colors_m = ["зеленого", "красного", "желтого", "белого", "черного"]
    animals = ["крысы", "коровы", "тигра", "зайца", "дракона", "змеи",
               "лошади", "овцы", "обезьяны", "курицы", "собаки", "свиньи"]
    cycle_year = (year - 1984) % 60
    c = cycle_year // 12
    a = cycle_year % 12
    color = colors_m[c] if a in (2, 3, 4) else colors_f[c]
    print(f"{year} - «год {color} {animals[a]}»")

if __name__ == '__main__':
    task10()
