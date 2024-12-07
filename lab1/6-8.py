def count_russian_chars(s):
    russian_count = len(list(filter(lambda x: "а" <= x <= "я" or "А" <= x <= "Я", s)))
    return russian_count


def all_latin_chars(s):
    latin_chars = list(filter(lambda x: "a" <= x <= "z", s))
    return latin_chars



def min_number_in_string(s):
    min_num = float('inf')
    curr_num = ""
    for char in s:
        if char == "-" and (curr_num == "" or curr_num == "-"):
            curr_num = "-"
        elif char.isdigit():
            curr_num += char
            min_num = min(min_num, int(curr_num))
        else:
            curr_num = ""
    
    return None if min_num == float('inf') else min_num


num = int(input(("Введите номер метода:\n1 - Количество русских символов\n2 - Все строчные символы латиницы\n3 - Минимальное целое число в строке\nНомер: ")))

match num:
    case 1:
        s = input("Введите строку: ")
        print(f"Результат метода: {count_russian_chars(s)}")
    case 2:
        s = input("Введите строку: ")
        print(f"Результат метода: {all_latin_chars(s)}")
    case 3:
        s = input("Введите строку: ")
        print(f"Результат метода: {min_number_in_string(s)}")
