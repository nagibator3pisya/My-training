# Таблица 1

# size = int(input())
#
# for row in range(size):
#     for col in range(3):
#         print(size, end=' ')
#
#     print()

# Таблица 2

# size = int(input())
# for row in range(1, size+1):
#     for col in range(5):
#         print(row, end=' ')
#
#     print()

# Таблица 3

# size = int(input())
#
# for i in range(1, size+1):
#     for j in range(1, 10):
#         print(f'{i} + {j} = {i + j}',end='\n')
#     print()

# триугольник

# size = int(input())
# for i in range(1, size // 2 + 2):
#     print('*' * i)
#
# for j in range(size // 2, 0, -1):
#     print('*' * j)

# Численный треугольник 1

# size = int(input())
# for i in range(size+1):
#     for j in range(i):
#         print(i, end='')
#     print()


# Численный треугольник 2
# size = int(input())
# count = 1
# for i in range(1, size+1):
#     for j in range(1,i +1):
#         print(count,end=' ')
#         count += 1
#     print()

#
# size = int(input())
#
# for i in range(1, size + 1):
#     for j in range(1, i + 1):
#         print(j, end='')  # Вывод возрастающих чисел
#     for k in range(i - 1, 0, -1):
#         print(k, end='')  # Вывод убывающих чисел
#     print()  # Переход на новую строку

# a = int(input())
# b = int(input())
# max_sum = 0 # cумма делителей
# max_i = 0 # максимальное значение
# for i in range(a,b+1): # проходит от 1 2 3 ... n +1
#     sum = 0 # сравнивание суммы
#     for j in range(1, i +1):  # цикл который будет делить число на другое и првоерять его остаток
#         if i % j == 0: # 1/ 1, 1 / 2 ... ищем делитель
#             sum += j # складываем числа что бы найти макс значение
#             if sum >= max_sum:
#                 max_sum = sum
#                 max_i = i
#
# print(max_sum,max_i)

# Делители 2

# n = int(input())
# for i in range(1,n +1):
#     count = 0
#     for j in range(1, i +1):
#         if i % j == 0:
#             count += 1
#
#     print(i, '+' * count, sep='')

# n = int(input())
#
# while n > 9:
#     sums = 0
#     for digit in str(n):
#         sums += int(digit)
#     n = sums
#
#
# print(n)

# cумма факториало
# from math import  factorial
# n = int(input())
# total = 0
#
# for i in range(1, n + 1):
#
#      total += factorial(i)
#
# print(total)


# n = int(input())
# factorial = 1
# factorial_sum= 0
#
# for i in range(1, n + 1):
#     factorial *= i
#     factorial_sum += factorial
#
#
# print(factorial_sum)


# Простые числа

a = int(input())
b = int(input())

for i in range(a, b+1):
    count = 0
    for j in range(1, i+1):
        if i % j == 0:
            count += 1
    if count == 2:
        print(i)

























