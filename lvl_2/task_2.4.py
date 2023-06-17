# Задача 2.4.

# Пункт A.
# Напишите функцию, которая удаляет все восклицательные знаки из заданной строк.
# Например,
# foo("Hi! Hello!") -> "Hi Hello"
# foo("") -> ""
# foo("Oh, no!!!") -> "Oh, no"

# Решение задачи пункта А
def remove_exclamation_marks(s: str):
    '''
    Функция удаляет все восклицательные знаки из заданной строки.
    :param s: заданная строка типа str.
    :return: возвращаемая строка типа str.
    '''
    return s.replace('!', '')


# Пункт B.
# Удалите восклицательный знак из конца строки.
# remove("Hi!") == "Hi"
# remove("Hi!!!") == "Hi!!"
# remove("!Hi") == "!Hi"

# Решение задачи пункта В
def remove_last_em(s):
    if s[len(s) - 1] == '!':
        return remove_last_em(s[:-1])
    else:
        return s


# Дополнительно

# Пункт С.
# Удалите слова из предложения, если они содержат ровно один восклицательный знак.
# Слова разделены одним пробелом.
# Например,
# remove("Hi!") === ""
# remove("Hi! Hi!") === ""
# remove("Hi! Hi! Hi!") === ""
# remove("Hi Hi! Hi!") === "Hi"
# remove("Hi! !Hi Hi!") === ""
# remove("Hi! Hi!! Hi!") === "Hi!!"
# remove("Hi! !Hi! Hi!") === "!Hi!"

# Решение задачи пункта С
def remove_word_with_one_em(s):
    s_spl = s.split()
    res_lst = []

    for i in s_spl:
        if i.count('!') != 1:
            res_lst.append(i)

    return ' '.join(res_lst)


# s = "Hi! !Hi! Hi!"

# print(remove_word_with_one_em(s))
