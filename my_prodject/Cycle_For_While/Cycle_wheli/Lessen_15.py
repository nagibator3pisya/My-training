# цикл частично моделирует эл. часы

# for seconds in range(60):
#     print(seconds)


# добавляем переменную minutes, вложенного цикла
from time import *
# for minutes in range(60):
#     for seconds in range(60):
#         print(f'{minutes} : {seconds}')


# ещё делаем цикл вложенный с переменной hours

# for hours in range(24):
#     for minutes in range(60):
#         for seconds in range(60):
#             xv = f'{hours}:{minutes} : {seconds}'
#             print(xv)

# # вложенный цикл for
# for i in range(1,5):
#     print(f'Итерация №{i}', sep='\n')
#     for j in range(1,5):
#         print(f'вложенный цикл №{i}.{j}' )

# for i in range(1,4):
#     for j in range(10,13):
#         print(i,j)




# вложенный цикл while
#
# i = 0
# j = 0
#
# while i <= 5:
#     while j <= 5:
#         print(f'вложенный цикл №{i}.{j}' )
#         j += 1
#     i += 1  # Увеличиваем i после вложенного цикла
#     print(f'Итерация №{i}', sep='\n')
#     j = 1  # Сбрасываем значение j к 1 для следующей итерации

# i = 1
#
# while i <= 3:
#     j = 1
#     while j <= 5:
#         print(f'{i} * {j} = {i * j} ', end='\t')
#         j += 1
#     print()
#     i += 1


# floor = 1 # этаж
# energy = 70 # энергия
# print(f'Я на этаже {floor} ')
#
# while floor != 5:
#     step = 0 # шаг
#     while step != 20:
#         step += 1
#         energy -= 1
#         if energy == 0:
#             print('Я устал, я немного отдохну')
#             energy += 70
#
#     floor += 1
#     print(f'Теперь я на этаже {floor}')
# print('Я добрался до нужного этажа')

# вывод треугольника
#
# row = 1 # ряд
# while row <= 5:
#     col = 1 # колонки
#     while col <= row:
#         print('*',end='')
#         col += 1
#     print()
#     row += 1
#
# i = 0
# while i <= 5:
#     # i += 1
#     print(i)
#     i += 1


# cброс счетчика в внутреннего цикла

# i = 1
# while i <= 3: # внешний
#     j = 1
#     while j <=5: # внутренний
#         print(f"{i} * {j} = {i * j}", end="\t")
#         j += 1
#     print()
#     i += 1
#     j = 1 # сброс счетчика внутреннего цикла

# for i in range(8):
#     for j in range(i + 1):
#         print('*',end='')
#     print()