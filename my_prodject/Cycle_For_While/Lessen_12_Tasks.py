from math import  *

# a = int(input())
# b = int(input())
# counter = 0
#
# for i in range(a, b+1):
#     q = i ** 3
#     if (q % 10 == 4) or (q % 10 == 9):
#        counter += 1
#
# print(counter)

# n = int(input())
# count = 0
# for i in range(n):
#     num = int(input())
#     count += num
# print(count)
# from math import *
#
# n = int(input())
# total = 0
#
# for i in range(1,n + 1):
#     total += 1 / i
#     # на первой итерации цикла как показано в задаче будет 1 / 1 = 1
# print(total - log(n))
from math import *


# counter += i
# n = int(input())
# sum = 0
# for i in range(1, n + 1):
#     kv = i ** 2
#     if kv % 10 == 2 or kv % 10 == 5 or kv % 10 == 8:
#         sum += i
#
# print(sum)

# n = int(input())
# total = 1
# for i in range(1 , n+1):
#     total *= i
#
# print(total )

# count = 1
# for  i in range(1,11):
#     num = int(input())
#     if num != 0:
#         count *= num
#
# print( count)

#
# n = int(input())
# count = 0  #  хранения суммы делителей.
# for i in range(1, n +1): # Цикл for проходит по числам от 1 до n включительно.
#     if n % i == 0: # роверяет, является ли i делителем n. Если остаток от деления n на i равен 0, то i является делителем.
#         count += i # Добавляет i к сумме count.
#
# print(count)

# num = int(input())
# total = 0
#
# for i in range(1, num + 1):
#     if i % 2 == 0:
#         total -= i
#     else:
#         total += i
#
# print(total)


n = int(input())
total1 = 0
total2 = 0

for i in range(1, n +1):
    num = int(input())
    if num > total1:
        total2 = total1
        total1 = num
    elif num > total2:
        total2 = num

print(total1, total2,sep='\n')

