"""
1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""


def division(number_1, number_2):
    """
    Возвращает частное от деления.

    Позиционные аргументы:
    number_1 -- делимое;
    number_2 -- делитель;
    """
    try:
        print(f'Результат деления: ', number_1 / number_2)
    except ZeroDivisionError:
        print('Деление на ноль!')


num_1 = float(input('Введиете делимое число: '))
num_2 = float(input('Введиете делитель число: '))

division(num_1, num_2)

"""
2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения, 
город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы. 
Реализовать вывод данных о пользователе одной строкой.
"""


def data(**kwargs):
    """
    Производит сбор данных пользователя по входящим параметрам.

    :param kwargs: Параметры опысывающие данные пользователя;
    :return: Возвращает словарь - 'Параметр':'Данные'
    """
    data_list = {}
    for el in kwargs:
        in_data = input(f'Введите {el}: ')
        data_list[el] = in_data
    return data_list


user_data = data(Имя='', Фамилия='', год_рождения='', город='', email='', num_phone='')
print(f'Имя: {user_data["Имя"]}, Фамилия: {user_data["Фамилия"]} , '
      f''f'год рождения: {user_data["год_рождения"]} , город: {user_data["город"]} , '
      f''f'e-mail: {user_data["email"]} , телефон: {user_data["num_phone"]} ')

"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, 
и возвращает сумму наибольших двух аргументов.
"""


def my_func(a, b, c):
    """
    Возвращает сумму наибольших двух аргументов.

    Позиционные аргументы:
    :param a: Некоторое число a;
    :param b: Некоторое число b;
    :param c: Некоторое число c;
    :return: сумма наибольших двух аргументов
    """
    min_num = min(a, b, c)
    sum_num = (a + b + c) - min_num
    return sum_num


num_1 = int(input(f'Введиете 1-e число: '))
num_2 = int(input(f'Введиете 2-e число: '))
num_3 = int(input(f'Введиете 3-e число: '))

sum_max = my_func(num_1, num_2, num_3)
print(f'Сумма наибольших двух аргументов - {sum_max}')

"""
3. Программа принимает действительное положительное число x и целое отрицательное число y. Необходимо выполнить 
возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y). При решении задания 
необходимо обойтись без встроенной функции возведения числа в степень.
Подсказка: попробуйте решить задачу двумя способами. 
Первый — возведение в степень с помощью оператора **. 
Второй — более сложная реализация без оператора **, предусматривающая использование цикла.

"""


def my_func(x, y):
    """
    Возвращает результат возведения числа Х в степень У, посредством оператора **.

    Позиционные аргументы:
    :param x: основание
    :param y: кол-во множителей (степень)
    :return: результат возведения в степень
    """
    result = x ** y
    return result


def my_func(x, y):
    """
    Возвращает результат возведения числа Х в степень У, посредством последовательного умножения
    числа х, у - раз.

    Позиционные аргументы:
    :param x: основание
    :param y: кол-во множителей (степень)
    :return: результат возведения в степень
    """
    count = 1
    z = x
    y = abs(y)
    while count < abs(y):
        z = z * x
        count += 1
    res = 1 / z
    return res


num = float(input('Введите положительное число: '))
exp = int(input('Введите целое отрицательное число: '))

print(my_func(num, exp))

"""
5. Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter должна выводиться 
сумма чисел. Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter. Сумма вновь 
введенных чисел будет добавляться к уже подсчитанной сумме. Но если вместо числа вводится специальный символ, 
выполнение программы завершается. Если специальный символ введен после нескольких чисел, то вначале нужно добавить 
сумму этих чисел к полученной ранее сумме и после этого завершить программу.
"""


def num_sum(in_list):
    """
    Возвращает сумму всех полученных чисел.

    :param in_list: Позиционный аргумент - список чисел
    :return: сумма всех числе
    """
    for el in in_list:
        num_list.append(int(el))
    res = sum(num_list)
    return res


print("Перед вами программа подсчета суммы чисел, введеных последовательно. \nДля завершения программы"
      " нажмите 'q'.")

num_list = []
result = 0

while True:
    num = input('Введите числа через пробел: ')
    usr_list = num.split()
    if usr_list[len(usr_list) - 1] != 'q':
        result = num_sum(usr_list)
        print(result)
    else:
        usr_list.remove('q')
        result = num_sum(usr_list)
        print(result)
        break

"""
6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же, но с прописной 
первой буквой. Например, print(int_func(‘text’)) -> Text. Продолжить работу над заданием. В программу должна попадать 
строка из слов, разделенных пробелом. Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной 
строки, но каждое слово должно начинаться с заглавной буквы. 
Необходимо использовать написанную ранее функцию int_func().

"""


def int_func(word):
    """
    Возвращает слово с заглавной буква вида -> 'Text'.

    :param word: Позиционный аргумент, слово
    :return: возвращает слово с заглавной буквы
    """
    word = word.capitalize()
    return word


some_word = input('Введите слово: ')
print(int_func(some_word))

words = input('Введите слова разделенные пробелами: ')
word_list = words.split()
result_list = []

for el in word_list:
    result_list.append(int_func(el))

print(' '.join(result_list))