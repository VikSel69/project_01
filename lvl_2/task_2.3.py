# Задача 2.3.

# Напишите функцию, которая принимает цифры от 0 до 9 и возвращает значение прописью.
# Например,
# switch_it_up(1) -> 'One'
# switch_it_up(3) -> 'Three'
# switch_it_up(10000) -> None
# Использовать условный оператор if-elif-else нельзя!

# Зешение задачи

def switch_it_up(number: int):
    """
    Функция возвращающая строковое название вводимых цифр.
    :param number: вводимая цифра типа int.
    :return: значение вводимоц цифры пропистью типа str.
    """
    NAME_NUMBER = ('Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine')
    try:
        return NAME_NUMBER[number]
    except IndexError:
        return 'None'

# print(switch_it_up(5))
