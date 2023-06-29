# Задача 4.1.
# Домашнее задание на SQL

# В базе данных teacher создайте таблицу Students

# Структура таблицы: Student_Id - Integer, Student_Name - Text, School_Id - Integer (Primary key)

# Наполните таблицу следующими данными:

# 201, Иван, 1
# 202, Петр, 2
# 203, Анастасия, 3
# 204, Игорь, 4

# Напишите программу, с помощью которой по ID студента можно получать информацию о школе и студенте.

# Формат вывода:

# ID Студента:
# Имя студента:
# ID школы:
# Название школы:

#  Решение задачи

import sqlite3

conn_to_db = sqlite3.connect('teacher.db')  # создаем соединение с БД
cursor = conn_to_db.cursor()


#  Блок кода формирующий БД для выполнения задачи.
#
# cursor.execute("""
#     CREATE TABLE School(
#         School_Id INTEGER PRIMARY KEY,
#         School_Name TEXT NOT NULL,
#         Place_Count INTEGER NOT NULL);
# """)
# cursor.execute("""
#     CREATE TABLE Students(
#         Student_Id INTEGER PRIMARY KEY,
#         Student_Name TEXT,
#         School_Id INTEGER NOT NULL);
# """)
# cursor.execute("""
#     INSERT INTO School(School_Id, School_Name, Place_Count)
#     VALUES  (1, 'Протон', 200),
#             (2, 'Перспектива', 300),
#             (3, 'Спектр', 400),
#             (4, 'Содружество', 500);
# """)
# cursor.execute("""
#     INSERT INTO Students(Student_Id, Student_Name, School_Id)
#     VALUES  (201, 'Иван', 1),
#             (202, 'Петр', 2),
#             (203, 'Анастасия', 3),
#             (204, 'Игорь', 4);
# """)

def get_student_by_id(student_id: int):
    """
    Метод возвращает данные по студенту, id которого указано в параметре
    :param student_id: id студента для поиска
    :return: tuple
    """
    query = """SELECT * FROM School JOIN Students ON School.School_Id = Students.School_Id
               WHERE Students.Student_Id = ?;"""
    cursor.execute(query, (student_id,))
    return cursor.fetchone()


def get_all_students():
    """
    Метод возвращает информацию по всем студентам из БД
    :return: list
    """
    query = """SELECT * FROM School JOIN Students ON School.School_Id = Students.School_Id;"""
    cursor.execute(query)
    return cursor.fetchall()


def print_student_by_id(student_id: int):
    """
    Метод выводит на консоль данные по студенту, id которого указано в параметре
    :param student_id: id студента для поиска
    :return: None
    """
    data_list = get_student_by_id(student_id)
    print('ID Студента:\t', data_list[3], '\n',
          'Имя студента:\t', data_list[4], '\n',
          'ID школы:    \t', data_list[0], '\n',
          'Название школы:\t', data_list[1], sep='')


def print_all_students():
    """
    Метод выводит на консоль данные по студентам из БД
    :return: None
    """
    data_list = get_all_students()
    print('ID Студента:\t', 'Имя студента:\t', 'ID школы:\t', 'Название школы:')
    for i in range(len(data_list)):
        print(str(data_list[i][3]).center(20), str(data_list[i][4]).ljust(15),
              str(data_list[i][0]).ljust(10), data_list[i][1])


#  Часть кода для выполнения тестов проверки выполнения заданных условий задачи.

print_student_by_id(201)
print()
print_all_students()
