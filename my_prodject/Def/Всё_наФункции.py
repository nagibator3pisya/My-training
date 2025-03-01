# def cub(edge_length: float) -> str:
#     return f'{3 * edge_length ** 2}'
#
#
#
# print(cub(5.6))

"""
Возвращает словарь, в котором ключ - это буква,
а значение - это количество повторений этой буквы в строке.
sequence.count(element) - возвращает количество элементов element в последовательности sequence
"""
from typing import *


#
# def letters(string: str) -> dict:
#     """
#     Функция для подсчета букв в слове
#     :param string: Строка для подсчета букв
#     :return: Словарь. Ключ - буква, значение - число
#     """
#     res_dict = {}
#     set_string = set(string)
#
#     for letter in set_string:
#         if letter != ' ':
#             count = string.count(letter)
#             res_dict[letter] = count
#
#     return res_dict
#
# strr = 'Аргентина манит негрА Аргентина манит негрА Аргентина манит негрА Аргентина манит негрА' \
#          'Аргентина манит негрА Аргентина манит негрААргентина манит негрА '
# print(letters(strr))

def get_key_value(dict_:dict,value:Any) -> dict:
    """
    Функция возвращает ключ и значение, соответствующий переданному значению.
    :param dict_: Словарь
    :param value: Значение
    :return: Словарь
    """
    for k,v in dict_.items():
        if v == value:
            return {k: v}


# Тестовый датасет
full_dict = {
    'title': 'Железный человек',
    'year': 2008,
    'director': 'Джон Фавро',
    'screenwriter': 'Марк Фергус и Хоук Остби, Артур Маркам и Мэтт Холлоуэй',
    'producer': 'Ави Арад и Кевин Файги',
    'stage': 'Первая фаза'
}

print(get_key_value(full_dict,'Джон Фавро'))