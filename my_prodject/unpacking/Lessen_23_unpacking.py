# распоковка списка
# list = [1, 2, 3, 4, 5]
# print(*list)
#
# print(iter('ffdfsdf'))  # str_ascii_iterator
# print(iter((1, 2, 3)))  # tuple_iterator
# print(iter(1)) # 'int' object is not iterable


# Распаковка списка с разделителем
#
# my_list = ['apple', 'banana', 'cherry','book']
# print(*my_list, sep=', ')

# Распаковка списков в переменные
#
# numbers = [1, 2, 3, 5, 6, 7]
# a,*b,c = numbers
#
# print(a,b,c , sep='\n')


# Распаковка с использованием _ для игнорирования некоторых значений

numbers = [1, 2, 3, 5]
a, _, _, d = numbers

print(a)
print(d)
