# генератор списков

# цикл
# list = []
#
# for i in range(10):
#     list.append(i)
#
# print(list) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# генератор списков
# list = [i for i in range(10)]
# print(list)


# простой генератор списков с строками
# str_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
# list = [int(i) for i in str_list]
#
# print(list)


# Создать список, заполненный квадратами целых чисел от 0 до 9 можно так:
# list = [int(i**2) for i in range(10)]
# print(list)


# Создать список, заполненный символами строки:
# list = [i for i in 'привет']
# print(list)


# подсчет строки с помощью len

# list_a = ['aaa','bbb','c']
# list_b = [len(x) for x in list_a]
# print(list_b)