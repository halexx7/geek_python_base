# -*- coding: utf-8 -*-

from math import factorial


def payroll(hours, rate_use, prize_use):
    """
    Возвращает сумму ЗП расчитанную по введенным данным, на конкретного сотрудника.

    Получаем именованные аргументы:
    :param hours: Отработано часов в месяце
    :param rate_use: Часовая ставка
    :param prize_use: Премия
    :return: Возвращает сумму ЗП
    """
    sum_pay = (hours * rate_use) + prize_use
    return sum_pay


def multiplic(prev_el, el):
    """
    Возвращает результат умножения текущего елемента на предыдущий некоторой последовательности

    Позиционные аргументы
    :param prev_el: предыдущий елемент последовательности
    :param el: текущий елемент
    :return: результат умножения
    """
    return prev_el * el


def generator(n):
    """ Возвращает генератор чисел от 1 до n """
    for elem in range(1, n + 1):
        yield elem


def fact(num_list):
    """
    Возвращает список факториалов входной последовательности

    :param num_list: последовательность натуральных чисел
    :return: список факториалов
    """
    num_fact = []
    for el in num_list:
        num_fact.append(factorial(el))
    return num_fact
