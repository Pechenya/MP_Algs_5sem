def task4():
    s = input("Введите строку для проверки на палиндром: ")
    text = s.lower().replace(" ", "")
    if palindrome(text):
        print(f"Строка \"{s}\" является палиндромом")
    else:
        print(f"Строка \"{s}\" не является палиндромом")

def palindrome(s):
    if len(s) <= 1:
        return True
    elif s[0] != s[-1]:
        return False
    else:
        return palindrome(s[1:-1])

if __name__ == '__main__':
    task4()
