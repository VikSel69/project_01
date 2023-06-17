import random
import datetime
import math

# Задача 1.2.

# Пункт A.
# Приведем плейлист песен в виде списка списков
# Список my_favorite_songs содержит список названий и длительности каждого трека
# Выведите общее время звучания трех случайных песен в формате
# Три песни звучат ХХХ минут

my_favorite_songs = [
    ['Waste a Moment', 3.03],
    ['New Salvation', 4.02],
    ['Staying\' Alive', 3.40],
    ['Out of Touch', 3.03],
    ['A Sorta Fairytale', 5.28],
    ['Easy', 4.15],
    ['Beautiful Day', 4.04],
    ['Nowhere to Run', 2.58],
    ['In This World', 4.02],
]

# Решение задачи 1.2 пункт А

sum_time = datetime.timedelta()

for i in random.sample(my_favorite_songs, 3):
    time_to_sec, time_to_min = math.modf(i[1])
    sum_time += datetime.timedelta(minutes=time_to_min, seconds=time_to_sec * 100)

print(f'Три песни звучат {sum_time} минут')

# Пункт B.
# Есть словарь песен
# Распечатайте общее время звучания трех случайных песен
# Вывод: Три песни звучат ХХХ минут.

my_favorite_songs_dict = {
    'Waste a Moment': 3.03,
    'New Salvation': 4.02,
    'Staying\' Alive': 3.40,
    'Out of Touch': 3.03,
    'A Sorta Fairytale': 5.28,
    'Easy': 4.15,
    'Beautiful Day': 4.04,
    'Nowhere to Run': 2.58,
    'In This World': 4.02,
}

# Решение задачи 1.2 пункт В

sum_time = datetime.timedelta()
key_lst = []

for key in my_favorite_songs_dict:
    key_lst.append(key)

for i in range(3):
    time_to_sec, time_to_min = math.modf(my_favorite_songs_dict[random.choice(key_lst)])
    sum_time += datetime.timedelta(minutes=time_to_min, seconds=time_to_sec * 100)

print(f'Три песни звучат {sum_time} минут')

# Дополнительно для пунктов A и B
# Пункт C.
# Сгенерируйте случайные песни с помощью модуля random
# import random

# Дополнительно
# Пункт D.
# Переведите минуты и секунды в формат времени. Используйте модуль datetime
