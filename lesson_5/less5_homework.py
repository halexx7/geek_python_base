__author__ = "Alexey_Khlybov"

import os
from lesson_5.less5_myfunc import num_sum, int_sum
import json

"""
1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем. 
Об окончании ввода данных свидетельствует пустая строка.
"""

# Подумать над очисткой или удалением файла после его показа

while True:
    text = input('Введите текст для записи в файл: \n')
    if text != '':
        with open("01_line_text.txt", "at") as f_obj:
            f_obj.write(text + '\n')
    else:
        with open("01_line_text.txt", "r") as f_obj:
            for line in f_obj:
                print(line)
        break

os.remove('01_line_text.txt')


"""
2. Создать текстовый файл (не программно), сохранить в нем несколько строк, 
выполнить подсчет количества строк, количества слов в каждой строке.
"""

with open('02_line_text.txt', 'r') as file:
    print(f'Кол-во строк в файле - {len(file.readlines())}')
    file.seek(0)
    count = 1
    for line in file:
        lines = line.split()
        print(f'Кол-во слов в строке "{count}" - {len(lines)}')
        count += 1


"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов 
(не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
Пример файла:
Иванов 23543.12
Петров 13749.32
"""


average = []
with open('03_employee_salary.txt', 'r') as file:
    for line in file:
        lines = line.split()
        lines[1] = float(lines[1])
        if lines[1] < 20000:
            print(f'{lines[0]} - {lines[1]}')
            average.append(lines[1])
    print(f'{(sum(average) / len(average)):.2f}')


"""
4. Создать (не программно) текстовый файл со следующим содержимым: 
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. При этом 
английские числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.
"""


trans_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
with open('04_data_in.txt', 'r+') as file:
    for line in file:
        lines = line.split()
        lines[0] = trans_dict.get(lines[0])
        with open('04_data_out.txt', 'a') as f_new:
            print(' '.join(lines), file=f_new)


"""
5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами. 
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""


with open('05_number.txt', 'w') as f_obj:
    f_obj.write(input('Введите числа через пробел: '))
    f_obj.seek(0)
    with open('05_number.txt', 'r') as f_obj_2:
        try:
            result = num_sum(f_obj_2.read().split())
            print(result)
        except ValueError:
            print('Ошибка! Не вся введенная последовательность является цифрами!')


"""
6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого предмета не обязательно 
были все типы занятий. Сформировать словарь, содержащий название предмета и общее количество занятий по нему. 
Вывести словарь на экран. Примеры строк файла: Информатика:   100(л)   50(пр)   20(лаб).
                                                   Физика:   30(л)   —   10(лаб)
                                              Физкультура:   —   30(пр)   —
Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

"""

dis_plan = {}
with open('06_subject.txt', 'r') as f_obj:
    for line in f_obj:
        line = line.replace('(', ' ')
        line = line.replace(':', ' ')
        lines = line.split()
        print(lines)
        dis_plan[lines[0]] = int_sum(lines)
    print(dis_plan)


"""
7. Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка должна содержать данные 
о фирме: название, форма собственности, выручка, издержки. Пример строки файла: firm_1   ООО   10000   5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила 
убытки, в расчет средней прибыли ее не включать.

Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью. 
Если фирма получила убытки, также добавить ее в словарь (со значением убытков). 
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].

Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджер контекста.
"""

with open('07_list_firm.txt', 'r') as f_obj:
    dict_prof = {}
    average = {}
    for line in f_obj:
        line = line.split()
        dict_prof[line[0]] = int(line[2]) - int(line[3])
    for el in dict_prof.values():
        average_profit = 0
        average = {}
        if el > 0:
            average_profit += el
        else:
            continue
        average['avarege_profit'] = average_profit
    result_list = [dict_prof, average]

# Сериализация в json
with open('07_list_firm.json', 'w', encoding='utf-8') as write_res:
    json.dump(result_list, write_res)

# Десериализация в json
with open('07_list_firm.json', 'r', encoding='utf-8') as read_res:
    test_js = json.load(read_res)
    print(test_js)
