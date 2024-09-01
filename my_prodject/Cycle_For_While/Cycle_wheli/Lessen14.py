# проверка на то что содержит ли введеное пользователем число 7

# num = int(input())
# number = num
# flag = False
# while num != 0:
#
#     last_digit = num % 10
#
#     if last_digit == 7:
#         flag = True
#         break
#     # num //= 10
#     num = int(input())
# if flag:  # эквивалентно if flag == True:
#     print('Число', number, 'содержит цифру 7')
# else:
#     print('Число', number, 'не содержит цифру 7')


#  проверяющую число на простоту: break

# num = int(input())
# flag = True
#
# for i in range(2,num):
#     if i % num == 0:
#         flag = False
#         break
#     elif i % num != 0:
#         flag = False
#         break
#
#
#
# if flag:
#     print('Число простое')
# else:
#     print('Число составное')

# cуммирование  чисел и если num < 0 то мы прирываем цикл
# result = 0
# for i in range(10):
#     num = int(input())
#     if num < 0:
#         break
#     result = result + num
# print(result)

# # бесконечный цикл
# import time
# i = 1
# while True:
#     print(f'Итерация {i}')
#     time.sleep(2)
#     i += 1

# вывод строки и так же её длинну в бесконечном цикле

while True:
    a = input()
    if a == 'exit':
        break
    print(a, len(a))

