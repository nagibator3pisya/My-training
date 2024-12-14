
''''
Картежы
'''''
# tuples = ()
# print(type(tuples))

'''
Пример картежев
'''
#
# empty_tuple = ()                                     # пустой кортеж
# point = (1.5, 6.0)                                   # кортеж из двух чисел
# names = ('Timur', 'Ruslan', 'Roman')                 # кортеж из трех строк
# info = ('Timur', 'Guev', 28, 170, 60, False)         # кортеж из 6 элементов разных
# # типов ('Timur', 'Guev', 28, 170, 60, False)
#
# nested_tuple = (('one', 'two'), ['three', 'four'])   # кортеж из кортежа и списка (('one', 'two'), ['three', 'four'])
#
# print(info)


'''
Кортеж с одним элементом
'''

# tuple = (1,)
# print(type(tuple))


'''
Изменяем значения в картеже
'''


my_tuple = (1, 'python', [1, 2, 3])

ss =  my_tuple[2][0] = 100
sss = my_tuple[2].append(17)

dsds = my_tuple[0] = 2

print(my_tuple)