''''
Вложенные списки
'''''

# matrix = [[i for i in range(6)] for j in range(5)]
# print(matrix)
# n = int(input()) # 5 вложенных списков
# m = int(input()) # 2 значения
# append = []
# for _ in range(n):
#     append.append([0] * m)
#
# print(append)
# lists = [
#
#  ["Тропик Рака", "Генри Миллер", 1934],
#
#  ["Преступление и наказание", "Федор Достоевский", 1866],
#
#  ["Окаянные дни", "Иван Бунин", 1926]
#
# ]
#
#
#
# for siblist in len(lists):
#     for row in len():
#         print(row, end=' ')
#     print()


# создание вложенного списка

# new_list = []
#
# for i in range(3):
#     nn_list = []
#     for j in range(3):
#         nn_list.append(i * j)
#     new_list.append(nn_list)
#
# print(new_list)

# однострочник

# считывание вложенных списков

# Считывание вложенного списка с клавиатуры
# rows = int(input("Введите количество строк: "))
# cols = int(input("Введите количество столбцов: "))
#
# nested_list = []
# for i in range(rows):
#     row = input(f"Введите элементы строки {i+1}, разделенные пробелом: ").split()
#     nested_list.append(row)
#
# print(nested_list)
#
#
# nested_list2 =[input(f"Введите элементы строки {i+1}, разделенные пробелом: ").split() for i in range(rows)]
# print(nested_list2)

'''
Доступ к элементам и изменения
'''
# list = [['1', '2', '3'], ['4', '5', '6']]
# nn = list[0][0] = 12
#
# print(list)
'''
Вывод элементов
'''
# list = [['1', '2', '3'], ['4', '5', '6']]

# for elem in list:
#     for j in elem:
#         print(j,end=' ')
#     print()
# ff= [elem for subs in list for elem in subs]
# print(*ff, end='')


'''
Пример считывание элементов 2й
'''

# n = 4 # кол во вложенных списков
# new_list = []
#
# for _ in range(n):
#     elem =[int(i) for i in input().split()] # int(i) конвертируем каждый эелемент в int  и считываем input().split()
#     # у нас получается строка
#     new_list.append(elem)
#
# print(new_list)
#
#
# n = 4 # кол во вложенных списков
# new_list = []
#
# for _ in range(n):
#     elem =[int(i) for i in input().split()] # int(i) конвертируем каждый эелемент в int  и считываем input().split()
#     # у нас получается строка
#     new_list.extend(elem)
#
# print(new_list)



'''
Перебор и вывод элементов вложенного списка
'''

# my_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# прозод по индексам
# for i in range(len(my_list)): # проходит по всей длине списка
#     for j in range(len(my_list[i])): # проходит по каждому индексу
#         print(my_list[i][j], end=' ')
#     print()

# перебор самих значений

# for i in my_list:
#     for j in i:
#         print(j, end=' ')
#     print()

'''
Подсчет суммы 
индексов
значений
'''

my_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# total = 0
# for i in range(len(my_list)):
#     for j in range(len(my_list[i])):
#         total += my_list[i][j]
#
# print(total)

# total = 0
#
# for i in my_list:
#     for j in i:
#         total += j
#
# print(total)
