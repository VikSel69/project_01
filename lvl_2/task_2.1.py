# Задача 2.1.

# Создайте две функции maximum и minimum,
# которые получают список целых чисел в качестве входных данных
# и возвращают наибольшее и наименьшее число в этом списке соответственно.
# Например,
# * [4,6,2,1,9,63,-134,566]         -> max = 566, min = -134
# * [-52, 56, 30, 29, -54, 0, -110] -> min = -110, max = 56
# * [42, 54, 65, 87, 0]             -> min = 0, max = 87
# * [5]                             -> min = 5, max = 5
# функции sorted, max и min использовать нельзя!

# Решение задачи

def minimum(arr: list):
    """
    Функция нахождения минимального числа в списке
    """
    min_number = arr[0]
    for i in arr:
        if i < min_number:
            min_number = i
    return min_number


def maximum(arr: list):
    """
    Функция нахождения максимального числа в списке
    """
    max_number = arr[0]
    for i in arr:
        if i > max_number:
            max_number = i
    return max_number


# print(minimum([-52, 56, 30, 29, -54, 0, -110]))
# print(maximum([-52, 56, 30, 29, -54, 0, -110]))
