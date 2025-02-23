# 10 раз
# def for_10():
#     for i in range(11):
#         print(f'{i}Python is awesome!')
#
# for_10()
# user = int(input())
# for i in range(1,user+1):
#     users = input()
#     print(i)



# def pow():
#     for i in range(10):
#         print('Python is awesome!')
#
# pow()

# def pow2(string,integer):
#     '''
#
#     :param string: cтрока которую нужно вывести
#     :param integer: кол-во раз которое нужно вывести строку
#     :return:
#     '''
#     for i in range(integer):
#         print(string)
#
#
# strs = input()
# ints = int(input())
#
# pow2(strs,ints)


# def pow_3(ints_string):
#
#     """
#
#     :param ints_string: ввод кол-во звезд
#     :return: вывод количество звезд в ряд
#     """
#
#     for _ in range(ints_string):
#         print('*' * 19)
#
#
# ints_str = int(input())
#
# pow_3(ints_str)


# def pow_4(user_string):
#     """
#
#     :param user_string: Ввод имени
#     :return: возвращает кол-во имени
#     """
#     for _ in range(10):
#         print(_,user_string)
#
#
# user = input()
# pow_4(user)


# def Square_number(nums):
#     """
#
#     :param nums:  Ввод числа сколько нужно получить квадратов от числа
#     :return: Возвращает квадраты
#     """
#     for i in range(nums+1):
#         kv = i ** 2
#         print(f"Квадрат числа {i} равен {kv}")
#
#
# nums_f = int(input())
# Square_number(nums_f)


# def until_the_end():
#     """
#     бесконечный ввод но при условии если пользователь не введет слово конец
#     :return:
#     """
#
#     while True:
#         text = input()
#         if text == 'КОНЕЦ' or text == ' конец':
#             break
#         print(text)
#
#
#
# until_the_end()



# text = input()
# sum = 0
# while text != 'стоп' and text != 'хватит' and text != 'достаточно':
#
#     sum += 1
#     text = input()
#
# print(sum)
# def sum_letter():
#
#     text = input()
#     sums = 0
#     while text != 'стоп' and text != 'хватит' and text != 'достаточно':
#         sums += 1
#         text = input()
#     return sums
#
#
# print(sum_letter())


# def sum_sharing(sums):
#     """
#
#     :param sums: - принмает число, если оно делатся на 7 то возвращает
#     :return:
#     """
#     while sums % 7 == 0:
#         print(sums)
#         sums = int(input())
#
#
# num = int(input())
# sum_sharing(num)

# integer = int(input())
# sum = 0
#
# while integer >= 0:
#     sum += integer
#     integer = int(input())
#
# print(sum)
#
# def sum_integer(sums):
#     sumss = 0
#     while sums >= 0:
#         sum += sums
#
#         sums = int(input())
#     return sumss
#
#
# ints = int(input())
#
# print(sum_integer(ints))


# def five(integ):
#     sums = 0
#     initial_value = integ
#     while 0 <= initial_value <= 5:
#         if initial_value == 5:
#             sums += 1
#         initial_value = int(input())
#     return sums
#
#
# int_five = int(input())
# print(five(int_five))



# stri = input()[::-1]
# for i in stri:
#     print(i)


#
# def reversesd(string_integer):
#     """
#
#     :param string_integer: строка чисел
#     :return: обратный порядок чисел
#     """
#     return string_integer[::-1]
#
#
#
# iss = input()
# data = reversesd(iss)
# print(data)

# вывод чисел в столб
# for i in data:
#     print(i)



# def mins(num):
#     return min(num)
#
# def maxs(num):
#     return max(num)
#
#
# data = input()
#
# print(f"Максимальная цифра равна {maxs(data)}")
# print(f"Минимальная цифра равна {mins(data)}")
# print(next())



# def find_max_min(num):
#     return min(num), max(num)
#
#
# data = input()
#
#
# numebrs = list(map(int, data.split()))
#
# max_num, min_num = find_max_min(numebrs)
#
# print('Мин' ,min_num)
# print('максимал', max_num)

# ПОСМОТРЕТЬ ЧТО ТАКОЕ MAP,FILTER,NEXT 

