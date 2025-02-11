# match case

# cmd = 'лево'

# match cmd:
#     case 'top':
#         print('Вверх')
#     case _:
#         print('Неизвестная кмд')

# поддерживает одно логическое определение, что бы сравнить несколько шаблонов
# match cmd:
#     case 'top' | 'upper':
#         print('вверх или вниз')
#     case 'left' | 'right':
#         print('Лево или в право')
#     case _:
#         print('Неизв. кмд')


# проверка на тип данных

# match cmd:
#     case str() as command:
#         print(f'Вы ввели {command}')
#     case _:
#         print('Неизвестно')


# Сравнение на несколько значений в match-case
# day = input().lower()
# match day:
#     case "суббота" | "воскресенье":
#         print("Это выходной день!")
#     case "понедельник" | "вторник" | "среда" | "четверг" | "пятница":
#         print("Это рабочий день.")
#     case _:
#         print("Неизвестный день.")


# Использование методов в match-case

# command = 'print_save'
#
# match command:
#     case cmd if cmd.startswith('print'):
#         print('Команда распечатать')
#     case cmd if cmd.startswith('print_save'):
#         print('Команда сохранить')
#     case _:
#         print('none')

# ещё один пример

# num = -10
#
# match num:
#     case n if n < 0:
#         print('отрицательное')
#     case n if n > 0:
#         print('положительное')
#     case n if n == 0:
#         print('число равно нулю')


# Использование match case type

# lists = [1,2,3]
#
# match lists:
#     case int()| float():
#         print('Числа')
#     case str():
#         print('Строки')
#     case list():
#         print('Это Список')
#     case _:
#         print(None)






