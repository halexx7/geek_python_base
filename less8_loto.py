from random import randint
__author__ = 'Aleksey Khlybov'

"""
== Лото ==

Правила игры в лото.

Игра ведется с помощью специальных карточек, на которых отмечены числа,
и фишек (бочонков) с цифрами.

Количество бочонков — 90 штук (с цифрами от 1 до 90).

Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр,
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:

--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86
--------------------------

В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается
случайная карточка.

Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.

Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
    Если цифра есть на карточке - она зачеркивается и игра продолжается.
    Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
    Если цифра есть на карточке - игрок проигрывает и игра завершается.
    Если цифры на карточке нет - игра продолжается.

Побеждает тот, кто первый закроет все числа на своей карточке.

Пример одного хода:

Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71
--------------------------
-- Карточка компьютера ---
 7 87     - 14    11
      16 49    55 88    77
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)

Подсказка: каждый следующий случайный бочонок из мешка удобно получать
с помощью функции-генератора.

Подсказка: для работы с псевдослучайными числами удобно использовать
модуль random: http://docs.python.org/3/library/random.html
"""


class LotoCard:

    def __init__(self, name):
        self._name = name
        bag = [b for b in range(1, 91)] # Наполняем мешок
        self._numbers_count = 15
        self.card = [__class__.get_number(bag), __class__.get_number(bag), __class__.get_number(bag)]

    @staticmethod
    def get_number(bag):
        line = ['' for _ in range(9)]
        for x in range(8, 3, -1):
            elem = randint(0, x)
            while line[elem] != '':
                elem += 1
            line[elem] = bag.pop(randint(0, len(bag) - 1))
        return line

    def __str__(self):
        rez = '{:-^26}\n'.format(self._name)
        for x in range(3):
            rez += '{:>2} {:>2} {:>2} {:>2} {:>2} {:>2} {:>2} {:>2} {:>2}' \
                       .format(*self.card[x]) + '\n'
        return rez + '--------------------------\n'

    def __getitem__(self, item):
        return self.card[item]

    def try_line_num(self, number): # Проверяем на вхождение и зачеркиваем если есть такой номер
        for i in range(3):
            if number in self.card[i]:
                self.card[i][self.card[i].index(number)] = '-'
                self._numbers_count -= 1
                return True
        return False


class LotoGame:

    def __init__(self, human, computer):
        self._human = human
        self._computer = computer
        self._numbers_in_bag = [b for b in range(1, 91)]

    def _get_bar(self):
        """ Возвращает случайный бочонок из мешка"""
        number = self._numbers_in_bag.pop(randint(0, len(self._numbers_in_bag) - 1))
        return number

    def start(self):

        while len(self._numbers_in_bag) > 0:
            if self._computer._numbers_count < 1:
                print('Компьютер выиграл!')
                break
            elif self._human._numbers_count < 1:
                print('Игрок выиграл!')
                break
            else:
                print(self._human, self._computer)
                number = self._get_bar()
                print('Новый бочонок {}, осталось {}'.format(number, len(self._numbers_in_bag)))
                issue = input('На карточке есть такое число? (y/n): ')
                if issue == 'y':
                    # Проверяем не ошибся ли игрок, когда говорил, что есть такой бочонок, а если есть зачеркиваем
                    if not self._human.try_line_num(number):
                        print('Игрок проиграл!')
                        break

                elif issue == 'n':
                    # Проверяем не ошибся ли игрок, когда говорил, что нет такого бочонока, а если нет проверяем у
                    # компьютера
                    if self._human.try_line_num(number):
                        print('Игрок проиграл!')
                        break
                    else:
                        self._computer.try_line_num(number)
                else:
                    print('Вы ввели не корректный символ!')
                    break


human_player = LotoCard(input('Введите имя игрока: '))
ii_player = LotoCard('Компьютер')

game = LotoGame(human_player, ii_player)
game.start()






