# cчитывает 10 чисел и определяет сколько из них больше 10.

# counter = 0
#
# for _ in range(10):
#     num = int(input())
#     if num > 10:
#         if num > 10:
#             counter = counter + 1
# print('Было введено', counter, 'чисел, больших 10.')




# счет 10 числен и определяет сколько из них больше 10 + сколько было
# введено 0- нулей

# counter = 0
# counter_2 = 0
# for _ in range(10):
#     num = int(input())
#     if num > 10:
#         counter = counter + 1
#     if num == 0:
#         counter_2 += 1
#
# print('Было введено', counter, 'чисел, больших 10.')
# print(f'Было введено, {counter_2} нулей')


# подсчитать количество
# чисел из диапазона [1;100],
# квадрат которых оканчивается на 4

# counter = 0
# for i in range(1,101):
#     if i ** 2 % 10 == 4:
#         counter += 1
#
# print(counter)

# счет + вывести общую сумму подсчетов

# count = 0
# for i in range(10):
#     num = int(input())
#     if num > 10:
#         count += num
#         print('сумма ушла в плюс на 10, сейчас у вас', count)
#     elif num < 10:
#         count -= num
#         print(f'сумма ушла в минус на 10, сейчас у вас {count}')
#     elif num == 10:
#         count = num
#         print(f'сумма равна 10, сейчас у вас {count}')

# Напишем программу, которая считает сумму натуральных чисел от 1 до 100
#
# total = 0
# for i in range(1, 101):
#     total += i
#     print(f'Текущая сумма: {total}  (добавлено {i})')
#
# print(f'Сумма равна {total}')

# которая запрашивает 10 целых чисел и находит их среднее значение

# total = 0
# for _ in range(10):
#     num = int(input())
#     total += num
# average = total / 10
# print('Среднее значение равно', average)


