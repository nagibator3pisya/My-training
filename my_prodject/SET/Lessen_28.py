
'''
Создание множества
'''

'''
Создание пустого сета
'''
# sets = set()

'''
пример
'''
# number = {1,2,3,4,5,6,7}
# print(number)
# str = {'a','b','c','d'}
# print(str)

'''
несколько типов данных
'''

# info = {'раз',1}
# print(info)


'''
set в разные типы
'''

# my_set1 = set(range(5))
# my_set2 = set('abc')
# my_set3 = set((1,2,4,5,6))
# my_set4 = set([1,2,4,5])
#
# print(my_set1)
# print(my_set2)
# print(my_set3)
# print(my_set4)

#
# emptyset1 = set([])  # пустое множество из пустого списка
# emptyset2 = set('')  # пустое множество из пустой строки
# emptyset3 = set(())  # пустое множество из пустого кортежа
#
# print(emptyset1)
# print(emptyset2)
# print(emptyset3)

'''
Не содеражт сеты дубликатов
'''
# my_set1 = {1,1,2,2,4,4,5,5,6,6}
# my_set2 = set('abbbssaaasscccc')
#
#
# print(my_set1)
# print(my_set2)
#
# '''
# перебор циклом
# '''
#
# numbers = {1,2,3,4,5}
#
# for i in numbers:
#     print(i)

# show_lst = ['apple', 'banana', 'orange', 'apple', 'banana']
# show_set = set(show_lst)
# print(show_set)
# print(' '.join(show_set))



# myset2 = set([1, 2, 2, 3, 3, 4, 4, 5, 5])
# print(len(myset2))

# film_set = {
#     'Железный человек',
#     'Невероятный Халк',
#     'Железный человек 2',
#     'Тор',
#     'Первый мститель',
#     'Мстители',
#     'Железный человек 3',
#     'Тор 2: Царство тьмы',
#     'Первый мститель: Другая война',
#     'Стражи Галактики',
#     'Мстители: Эра Альтрона',
#     'Человек-муравей',
#     'Первый мститель: Противостояние',
#     'Доктор Стрэндж',
#     'Стражи Галактики. Часть 2',
#     'Человек-паук: Возвращение домой',
#     'Тор: Рагнарёк',
#     'Чёрная пантера',
#     'Мстители: Война бесконечности',
#     'Человек-муравей и Оса',
#     'Капитан Марвел',
#     'Мстители: Финал',
#     'Человек-паук: Вдали от дома',
#     'Чёрная вдова',
#     'Шан-Чи и легенда десяти колец',
#     'Вечные',
#     'Человек-паук: Нет пути домой',
#     'Доктор Стрэндж: В мультивселенной безумия',
#     'Тор: Любовь и гром',
#     'Чёрная пантера: Ваканда навеки',
#     'Человек-муравей и Оса: Квантомания',
#     'Стражи Галактики. Часть 3',
#     'Капитан Марвел 2',
#     'Дэдпул 3',
#     'Капитан Америка: Дивный новый мир',
#     'Громовержцы',
#     'Блэйд',
#     'Фантастическая четвёрка',
#     'Мстители: Династия Канга',
#     'Мстители: Секретные войны',
#     'Безымянный фильм о Человеке-пауке',
#     'Безымянный фильм о Шан-Чи',
#     'Безымянный фильм о Вечных',
#     'Безымянный фильм о мутантах'
# }
#
# is_sorted = False
#
# while not  is_sorted:
#     user_input = input()


'''
множества методы
'''
# add() - добавить один элемент
# set1 = {1, 2, 4}
# set1.add(6)
# print(set1)

# update() - добавить несколько
# set_2 = {1,2,3,4}
# set_2.update({5,6})
# print(set_2)

'''
удаление
'''

# set1 = {1, 2, 3, 4, 'a', 'p'}

# set1.remove(1)
# print(set1)

# set1.discard(5)
# print(set1)

# """
# рандомный фильм через pop
# """
# from marvel import simple_set
# flag = False
# while not flag:
#     film = input()
#     if film != 'exti':
#         films = simple_set.pop()
#         print(films)
#     else:
#         flag = True


# математические множества

# Методы множеств (математические)
# union - объединяет множества (оператор | )
# intersection - возвращает пересечение множеств (оператор &)
# difference - возвращает разность множеств (оператор -)
# symmetric_difference - возвращает симметричную разность множеств (оператор ^)
# film_olga = {
#     'Железный человек',
#     'Невероятный Халк',
#     'Железный человек 2'}
#
# film_alex =  {
#     'Тор',
#     'Первый мститель',
#     'Мстители',
#     'Железный человек 3',
#     'Тор 2: Царство тьмы',
#     'Железный человек 2'
#     }

# unions = simple_set.union(simple_set2)
# unions2 = simple_set|simple_set2 # 2 вариант объединения
# print(unions2)

# Какие фильмы смотрели оба?
# print(film_alex.intersection(film_olga))

# print(film_olga.difference(film_alex))

# print(film_olga.symmetric_difference(film_alex))



# while True:
#     user = input()
#     if user  == 'стоп':
#         break
#     usser_film = set(user.split(',')) # приобразум в ser , разделяя запятым
#     out = usser_film.intersection(simple_set)
#     if out:
#         print(''.join(out)) # приобразуем в строку
#     else:
#         print('Такого нет')


# со списком

# while True:
#     user = input()
#     if user  == 'стоп':
#         break
#     usser_film = user.split(',')
#     bd_list = list(simple_set)
#     a = [i for i in usser_film if i in bd_list]
#     if a:
#         print(a)
#     else:
#         print('такого нет')
