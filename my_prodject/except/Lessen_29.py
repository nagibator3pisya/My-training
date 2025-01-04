"""""
Искоючение
"""""
from pickle import PickleError

# num_input = input('Число: ')
# num_list = num_input.split(',')
#
# new_list = []
#
# for i in num_list:
#     try:
#         i = int(num_input)
#     except ValueError:
#         print(f"Не число: {i}")
#         continue
#     finally:
#         new_list.append(i)
#
# print(new_list)

'''
Делим 2 числа друг на друга
'''
# a = input()
# b = input()
#
# try:
#     int_a = int(a)
#     int_b = int(b)
#     print(int_a / int_b)
# except ValueError: # Возникает если это не число
#     print('Это не число')
# except ZeroDivisionError as err: # Деление на 0 запрещено
#     print(f'Делить на ноль нельзя: {err}')
# else: # выполняется если ошибок нет
#     print('Ошибок нет')
# finally: # блок всегда выполняется
#     print('Блок выполняется всегда')

'''
Несколько исключений
'''
# flag = False
# while not flag:
#     try:
#         inputs = int(input())
#         result = 10 / inputs
#         my_list = [0, 1, 2, 3]
#         print(10 / my_list[inputs])
#     except ValueError:
#         print('Не число')
#     except ZeroDivisionError:
#         print('Делить на ноль нельзя')
#     except IndexError:
#         print('Индекс выходит за приделы списка')
#     else:
#         flag = True
'''
Обьеденяем ошибки ещё часть 2
'''
# flag = False
# while not flag:
#     try:
#         inputs = int(input())
#         result = 10 / inputs
#         my_list = [0, 1, 2, 3]
#         print(10 / my_list[inputs])
#     except(ValueError,ZeroDivisionError,IndexError) as e:
#         print(f'Произошла ошибка {e}')
#     else:
#         flag = True

'''
Обработка всех типов исключений
'''

flag = False
while not flag:
    try:
        inputs = int(input())
        result = 10 / inputs
        my_list = [0, 1, 2, 3]
        print(10 / my_list[inputs])
    except Exception as e:
        print(f'Произошла ошибка {e}')
    else:
        flag = True.