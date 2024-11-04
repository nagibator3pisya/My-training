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

numbers = int(input())
string = []
for i in range(numbers):
    sting_gogle = input()
    string.append(sting_gogle)



chear = input()

for j in string:
    if chear.lower() in j.lower():
        print(j)
    else:
        continue



#
# poists = input()
# poist = []
#
# for j in string:
#     if poists in j:
#         poist.append(j)
#
# print(poist)





