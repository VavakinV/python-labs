import random


def shuffle_words(s):
    words = s.split()
    random.shuffle(words)
    return ' '.join(words)


def count_even_length_words(s):
    words = s.split()
    even_count = len(list(filter(lambda x: len(x)%2==0, words)))
    return even_count


def tricolor(s):
    words = s.split()
    words.sort(key=lambda x: 2 if x=='красный' else 1 if x=='синий' else 0 if x=='белый' else 3)
    return ' '.join(words)

num = int(input(("Введите номер метода:\n1 - Перемешивание слов\n2 - Количество слов с четным количеством символов\n3 - Упорядочивать цвета российского флага\nНомер: ")))

match num:
    case 1:
        s = input("Введите слова через пробел: ")
        print(f"Результат метода: {shuffle_words(s)}")
    case 2:
        s = input("Введите слова через пробел: ")
        print(f"Результат метода: {count_even_length_words(s)}")
    case 3:
        s = input("Введите цвета через пробел: ")
        print(f"Результат метода: {tricolor(s)}")
