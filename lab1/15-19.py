def global_max(array, index):
    if index < 0 or index >= len(array):
        return False

    element = array[index]

    return all(element >= e for e in array)  


def local_min(array, index):
    if index < 0 or index >= len(array):
        return False

    element = array[index]

    is_left_min = index == 0 or element < array[index - 1]
    is_right_min = index == len(array) - 1 or element < array[index + 1]

    return is_left_min and is_right_min


def shift_left(array):
    if len(array) == 0:
        return
    array.append(array.pop(0))


def print_even_and_odd(array):
    even_indexes = [x * 2 for x in range((len(array) + 1) // 2)]
    odd_indexes = [x + 1 for x in even_indexes]

    print("На четных индексах: ", end="")
    print(" ".join(str(array[i]) for i in even_indexes))
    
    print("На нечетных индексах: ", end="")
    print(" ".join(str(array[i]) for i in odd_indexes if i < len(array))) 

print("Выберите метод:\n1 - Проверка на глобальный максимум\n2 - Проверка на локальный минимум\n3 - Циклический сдвиг влево на 1\n4 - Вывод элементов сначала с четными индексами, затем - с нечетными")
method_num = int(input("Введите номер: "))

if method_num == 1:
    input_array = input("Введите элементы массива, разделенные пробелами: ")
    array = list(map(int, input_array.split()))
    i = int(input(f"Введите индекс элемента для проверки (от 0 до {len(array) - 1}): "))
    if global_max(array, i):
        print(f"Элемент по индексу {i} является глобальным максимумом.")
    else:
        print(f"Элемент по индексу {i} не является глобальным максимумом.")

elif method_num == 2:
    input_array = input("Введите элементы массива, разделенные пробелами: ")
    array = list(map(int, input_array.split()))
    i = int(input(f"Введите индекс элемента для проверки (от 0 до {len(array) - 1}): "))
    if local_min(array, i):
        print(f"Элемент по индексу {i} является локальным минимумом.")
    else:
        print(f"Элемент по индексу {i} не является локальным минимумом.")

elif method_num == 3:
    input_array = input("Введите элементы массива, разделенные пробелами: ")
    array = list(map(int, input_array.split()))
    shift_left(array)
    print("Массив после сдвига:")
    print(array)

elif method_num == 4:
    input_array = input("Введите элементы массива, разделенные пробелами: ")
    array = list(map(int, input_array.split()))
    print_even_and_odd(array)

