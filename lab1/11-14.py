import re
num = int(input(("Введите ключ сортировки:\n1 - Разница между частотой наиболее часто встречаемого символа в строке и частотой его появления в алфавите.\n2 - Квадратичное отклонение частоты встречаемости самого часто встречаемого символа от частоты его встречаемости в текстах на этом алфавите\n3 - Разница между количеством сочетаний 'гласная-согласная' и 'согласная-гласная'\n4 - Квадратичное отклонение частоты встречаемости самого распространенного символа в наборе строк от частоты его встречаемости в данной строке\nНомер: ")))

english_frequencies = {'a': 0.82, 'b': 0.015, 'c': 0.028, 'd': 0.043, 'e': 0.127, 'f': 0.022, 'g': 0.02, 'h': 0.061, 'i': 0.07, 'j': 0.0015, 'k': 0.0077, 'l': 0.04, 'm': 0.024,'n': 0.067,'o': 0.075,'p': 0.019,'q': 0.00095,'r': 0.06,'s': 0.063,'t': 0.091,'u': 0.028,'v': 0.0098,'w': 0.024,'x': 0.0015,'y': 0.02, 'z': 0.00074}
russian_frequencies = {'а': 0.0801,'б': 0.0159,'в': 0.0454,'г': 0.017,'д': 0.0298,'е': 0.0845,'ё': 0.0004, 'ж': 0.0094,'з': 0.0165,'и': 0.0735,'й': 0.0121,'к': 0.0349,'л': 0.044,'м': 0.0321,'н': 0.067,'о': 0.1097,'п': 0.0281,'р': 0.0473,'с': 0.0547,'т': 0.0626,'у': 0.0262,'ф': 0.0026,'х': 0.0097,'ц': 0.0048,'ч': 0.0144,'ш': 0.0073,'щ': 0.0036,'ъ': 0.0004,'ы': 0.019,'ь': 0.0174,'э': 0.0032,'ю': 0.0064,'я': 0.0201}

english_vowels = 'aeiouy'
english_consonants = 'bcdfghjklmnpqrstvwxz'
russian_vowels = 'аеёиоуыэюя'
russian_consonants = 'бвгджзйклмнпрстфхцчшщъь'

def most_frequent_frequency(string):
    most_common, most_commmon_frequency = most_frequent(string)
    if most_common in english_frequencies.keys():
        return most_commmon_frequency - english_frequencies[most_common]
    elif most_common in russian_frequencies:
        return most_commmon_frequency - russian_frequencies[most_common]
    else: 
        return -1

def letter_frequencies(string):
    letters = list(filter(lambda x: "а" <= x <= "я" or "А" <= x <= "Я" or "a" <= x <= "z" or "A" <= x <= "Z", string))
    letters = list(map(lambda x: x.lower(), letters))
    letters_num = len(letters)
    frequencies = {}
    for letter in letters:
        if letter in frequencies:
            frequencies[letter] += 1/letters_num
        else:
            frequencies[letter] = 1
    return frequencies

def most_frequent(string):
    frequencies = letter_frequencies(string)
    sorted_frequencies = sorted(frequencies.items(), key=lambda x:x[1], reverse=True)
    most_common, most_commmon_frequency = sorted_frequencies[0][0], sorted_frequencies[0][1]
    return most_common, most_commmon_frequency

def cons_vow_vow_cons_diff(string):
    prev = 1 if (string[0] in english_consonants or string[0] in russian_consonants) else 0 if (string[0] in english_vowels or string[0] in russian_vowels) else None
    cons_vow = 0
    vow_cons = 0
    for i in range(1, len(string)):
        if prev == 1 and (string[i] in english_vowels or string[i] in russian_vowels):
            cons_vow += 1
        elif prev == 0 and (string[i] in english_consonants or string[i] in russian_consonants):
            vow_cons += 1
        if (string[i] in english_vowels or string[i] in russian_vowels):
            prev = 0
        elif (string[i] in english_consonants or string[i] in russian_consonants):
            prev = 1
        else:
            prev = None
    return abs(cons_vow - vow_cons)

strings = []
match num:
    case 1:
        s = input("Введите строки: ")
        while s != "":
            strings.append(s)
            s = input()
        strings.sort(key=lambda x: most_frequent_frequency(x))
        print("Отсортированные строки: ")
        print(*strings, sep="\n")
    case 2:
        s = input("Введите строки: ")
        while s != "":
            strings.append(s)
            s = input()
        strings.sort(key=lambda x: most_frequent_frequency(x)**2)
        print("Отсортированные строки: ")
        print(*strings, sep="\n")
    case 3:
        s = input("Введите строки: ")
        while s != "":
            strings.append(s)
            s = input()
        strings.sort(key=lambda x: cons_vow_vow_cons_diff(x))
        print("Отсортированные строки: ")
        print(*strings, sep="\n")
    case 4:
        s = input("Введите строки: ")
        while s != "":
            strings.append(s)
            s = input()
        mf, mf_frequency = most_frequent(" ".join(strings))
        strings.sort(key=lambda x: (mf_frequency - (0 if not (mf in letter_frequencies(x).keys()) else letter_frequencies(x)[mf]))**2)
        print("Отсортированные строки: ")
        print(*strings, sep="\n")