# вывод каждого элемента

# numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# for i in numbers:
#     print(i)

# for i,y in enumerate(numbers):
#     print(i,y)

# перебор с помощью цикла while

# index = 0
# while index < len(numbers) and numbers[index] != 3:
#     print(numbers[index])
#     index += 1

# найти среднию длинну списка
# my_list = [1, 2, 3, 4, 5]
# total = 0
# for element in my_list:
#     total += element
# average = total / len(my_list)

# numbers = [1, 78, 23, -65, 99, 9089, 34, -32, 0, -67, 1, 11, 111]
# li = []
#
# for i in numbers:
#     li.append(i**2)
#
# print(sum(li))

# Значение функции
# numbers = int(input())
# result1 = []
# result2 = []
# for i in range(numbers):
#     n = int(input())
#     # s = (n+1)**2
#     result1.append((n+1)**2)
#     result2.append(n)
#
# print(*result2, sep='\n')
# print()
# print(*result1, sep='\n')

# Remove outliers
# numbers = int(input())
# list = []
# for i in range(numbers):
#     num = int(input())
#     list.append(num)
#
# list.remove(min(list)) or list.remove(max(list))
# print(*list,sep = '\n')
#


# Без дубликатов
# numbers = int(input())
# element = []
# for i in range(numbers):
#     sting = input()
#     element.append(sting)
#
# unical = []
#
# for e in element:
#     if e not in unical:
#         unical.append(e)
#
# print(*unical,sep='\n')
# второй вариант но он не подходит
# sets = [input() for _ in range(int(input()))]
# r = set(sets)
# print(*r,sep ='\n')

# Google search - 1
# numbers = int(input())
# string = []
# for i in range(numbers):
#     sting_gogle = input()
#     string.append(sting_gogle)
#
# print(string)
#
# chear = input()
#
# for j in string:
#     if chear.lower() in j.lower():
#         print(j)
#     else:
#         continue




# Google search - 2

'''
    идет кол во строк число
    далее количество строк по числу вывод

    k — количество поисковых запросов
    и вывод k строк — поисковые запросы
'''

# numbers = int(input())
# string = []
# for i in range(numbers):
#     sting_gogle = input()
#     string.append(sting_gogle)
#
#
# chear = input()
# # k_int = int(input())
# for j in string:
#     if chear.lower() in j.lower():
#         print(j)
#     else:
#         continue


# nubers = int(input()) # Вводим количество строк
#
# a_sting = [] # Список для строк
# b_chear_reqvest = [] # Список для поисковых запросов
# c = [] # Список для строк, содержащих все запросы
#
# for i in range(nubers):
#   string = input() # Вводим строку
#   a_sting.append(string) # Добавляем строку в список
#
# k_nub = int(input()) # Вводим количество поисковых запросов
#
# for _ in range(k_nub): # Вводим поисковые запросы
#   chear_reqvest = input()
#   b_chear_reqvest.append(chear_reqvest.lower()) # Добавляем запрос в нижнем регистре
#
# # Проверка на наличие всех запросов в каждой строке
# for u in range(len(a_sting)):
#   count = 0
#   for j in b_chear_reqvest:
#     if j in a_sting[u].lower(): # Проверяем, содержится ли запрос в строке
#       count += 1
#   if count == len(b_chear_reqvest): # Если все запросы найдены
#     c.append(a_sting[u]) # Добавляем строку в список c
#
# # Выводим список c
# print(*c, sep='\n')



# Negatives, Zeros and Positives

numbers = int(input())
negative_results = [] # отрицательные
zero = [] # нули
positive_numbers = [] # положительные

for i in range(numbers):
    numbers_s = int(input())
    if numbers_s < 0:
        negative_results.append(numbers_s)
    elif numbers_s == 0:
        zero.append(numbers_s)
    else:  # number > 0
        positive_numbers.append(numbers_s)

print(*negative_results, sep='\n')
print(*zero, sep='\n')
print(*positive_numbers, sep='\n')