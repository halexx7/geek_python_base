__author__ = "Alexey_Khlybov"


def num_sum(in_list):
    """
    Возвращает сумму последовательности.

    :param in_list: Позиционный аргумент - список чисел
    :return: сумма всех числе
    """
    num_list = []
    for el in in_list:
        num_list.append(int(el))
    result = sum(num_list)
    return result


def int_sum(in_list):
    """
    Возвращает сумму ЧИСЕЛ последовательности.

    :param in_list: Позиционный аргумент - некая последовательность (не обязательно чисел)
    :return: сумма всех чисел последовательности
    """
    num_list = []
    for el in in_list:
        try:
            num_list.append(int(el))
        except ValueError:
            continue
        result = sum(num_list)
    return result


if __name__ == '__main__':
    test_list = ['1', 'aaaa', '34', 'dsfsdf']
    print(num_sum_2(test_list))