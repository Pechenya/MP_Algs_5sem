def task6():
    s = input("Введите строку: ")
    print(" ".join(reverse_words(s.split())))

def reverse_words(words):
    if len(words) <= 1:
        return words
    else:
        return reverse_words(words[1:]) + [words[0]]

if __name__ == '__main__':
    task6()
