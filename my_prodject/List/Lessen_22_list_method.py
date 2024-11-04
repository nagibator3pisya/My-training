# Методы списокв и взаимодействия с ними
# append()
# fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
# fruits.append('Новый элемент')
# print(fruits)

# 2 пример с append()
#
# numbers = []
# numbers.append(1)
# numbers.append(2)
# print(numbers)

# с циклом
# for i in range(12):
#     numbers.append(i)
# print(numbers)

# extend()
# numbers = [0, 2, 4, 6, 8, 10]
# odds = [1, 3, 5, 7]
#
# numbers.extend(odds)
# print(numbers)

# Разница между extend() и append()

# words1 = ['iq option', 'stepik', 'beegeek']
# words2 = ['iq option', 'stepik', 'beegeek']
#
# words1.append('python')
# words2.extend('python')
# print(words1)
# print(words2)


# inn = input()
# lists = []
# for i in inn:
#     lists.extend(i)
#
# print(lists)

# del
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# del numbers[2]
# print(numbers)


# sort()
# numbers = [2,5,9,7,1,3,6]
# numbers.sort(reverse=True)
# print(numbers)

# Задачи

# numbers = [2, 6, 3, 14, 10, 4, 11, 16, 12, 5, 4, 16,
#            1, 0, 8, 16, 10, 10, 8, 5, 1, 11, 10, 10, 12, 0, 0, 6,
#            14, 8, 2, 12, 14, 5, 6, 12, 1, 2, 10, 14, 9, 1, 15, 1,
#            2, 14, 16, 6, 7, 5]
#
# # длина
# print(len(numbers))
#
# # last_elements
# print(numbers[-1:])
#
# # # reversed
# # print(numbers[::-1])
# #
# # # Вывел YES, если список содержит числа  5 и  17 и NO в противном случае;
# if 5 and 17 in numbers:
#     print('Yes')
# else:
#     print('NO')
# # # Вывел список с удаленными первым и последним элементами.
# del numbers[0]
# del numbers[-1:]
# print(numbers)



# Список строк

# numbers_strint = int(input())
# list = []
# for i in range(numbers_strint):
#     language = input()
#     list.append(language)
#     print(language)
#
#
# print(list)

# # Алфавит
# liters = input()
# lists = []
#
# for i in range(26):
#     lists.append(chr(ord('a') + i) * (i + 1))
#
# print(lists,end='')
# ['a', 'bb', 'ccc', 'dddd', 'eeeee', 'ffffff', 'ggggggg', 'hhhhhhhh', 'iiiiiiiii', 'jjjjjjjjjj', 'kkkkkkkkkkk', 'llllllllllll', 'mmmmmmmmmmmmm', 'nnnnnnnnnnnnnn', 'ooooooooooooooo', 'pppppppppppppppp', 'qqqqqqqqqqqqqqqqq', 'rrrrrrrrrrrrrrrrrr', 'sssssssssssssssssss', 'tttttttttttttttttttt', 'uuuuuuuuuuuuuuuuuuuuu', 'vvvvvvvvvvvvvvvvvvvvvv', 'wwwwwwwwwwwwwwwwwwwwwww', 'xxxxxxxxxxxxxxxxxxxxxxxx',
# 'yyyyyyyyyyyyyyyyyyyyyyyyy', 'zzzzzzzzzzzzzzzzzzzzzzzzzz']

# список кубов

# input_list_kubs = int(input())
# list_kubs = []
# for i in range(input_list_kubs):
#     numbers = int(input())
#     list_kubs.append(numbers**3)
#
# print(list_kubs)

# Список делителей

# numb = int(input())
# lists = []
# for i in range(1,numb + 1):
#     if numb % i == 0:
 #         lists.append(i)

#
 # print(lists)

# n1 = int(input())
# list1 = []
#
# for i in range(n1):
#     n2 = int(input())
#
#     list1.append(n2)
# del list1[1::2]
#
# copylist = list1.copy()
# print(copylist)


numbres = int(input())

# for i in range(numbres):
#     sting_list = input()
#     lists.extend(sting_list)




