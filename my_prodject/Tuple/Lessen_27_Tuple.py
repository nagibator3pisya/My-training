''''
Функция tuple() преобразования
'''''

# list = [1,2,3,4,5]
# tuple = tuple(list)
# print(tuple) # (1, 2, 3, 4, 5)


'''
Преобразования строки в картеж
'''

# string = 'привет'
#
# tuple_str = tuple(string)
# print(tuple_str)

# изменения 
# writer = ('Лев Толстой', 1827)
# a = list(writer)
# a[1] = 1985
# print(tuple(a)) # ('Лев Толстой', 1985)


'''
Особенности кортежей

Кортежи поддерживают те же операции, что и списки, за исключением изменяющих содержимое.

Кортежи поддерживают:

- доступ к элементу по индексу (только для получения значений элементов);
- методы, в частности index(), count();
- встроенные функции, в частности len(), sum(), min() и max();
- срезы;
- оператор принадлежности in;
- операторы конкатенации (+) и повторения (*).
'''

# доступ по индексу

# turtles = ('Mike', 'Leo', 'Don', 'Raph')
#
# print(turtles[0])
# print(turtles[2])

# вложенный картеж и доступ к нему

# input_box = ('firstbox', (15, 150))
# print(input_box[1][1])


'''
Оператор проверки in
'''
# song = ('Roses', 'are', 'Red')
#
# print('Привет' in song)
# print('Roses' in song)

'''
for цикл в кортежах
'''

# my_tuple = ('Wise', 'men', 'say', 'only', 'fools', 'rush', 'in')
# for i in my_tuple:
#     print(i)

'''
сортировка
'''

# sorteds = (100000, 100, 10, 10000, 1, 1000)
#
# print(tuple(sorted(sorteds)))

'''
удаление
'''

# some_useless_stuff = ('sad', 'bad things', 'trans fats')
# del some_useless_stuff
#
# print(some_useless_stuff)

'''
Cрезы
'''
# float_tuple = (1.1, 0.5, 45.5, 33.33, 9.12, 3.14, 2.73)
# print(float_tuple[1:3])
# print(float_tuple[1:])
# print(float_tuple[:1])


'''
Длинна
'''

# lens = ('ghb','ggg','gdfdf')
#
# print(len(lens))


'''
Конкатенация 
'''
#
'''
сложение
'''
# tuple1 = ('ggg',)
# tuple2 = ('aa',)
# tuple3 = ('dfsdf',)
#
# print(tuple1 + tuple3 + tuple2)
#
'''
остальные операции
'''
# nums = ((1,2,34) + (2,4,5))
# nums2 = ((1,2)*3)
# nums3 = ((0,) * 10)
# print(nums)
# print(nums2)
# print(nums3)

'''
доп операции += *= и тд
'''
#
# a = (1,2)
# b = (3,4,5)
#
# a += b
# b *= 5
# print(a)
# print(b)

'''
Индекс заданного элемента

Метод index() позволяет получить индекс элемента. 
Достаточно передать нужное значение элемента, как аргумент метода:
'''
# rom = ('I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X')
# print(rom.index('I'))


'''
Число вхождений 
метод count
'''
# AT = ('Finn', 'Jake', 'BiMo', 'Marceline', 'Princess Bubblegum', 'BiMo','Jake','Jake')
# print(AT.count('Jake'))


'''
Встроенные функции sum(), min(), max()
'''
# sum()
# numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# print(sum(numbers))
# print(f'минимальное', min(numbers))
# print(f'максимальное', max(numbers))

'''
Преобразование в разные типы
из tuple в str,list,dict
'''
# str
tuples = ('gfgdfg','dfgdss')
print(','.join(tuples))

# list
tuples2 = (1,2,3,4,5)
print(list(tuples2))

# dict

tuples3 = (('Joins',123),('Din',2233))

print(dict((x,y) for x,y in tuples3))




