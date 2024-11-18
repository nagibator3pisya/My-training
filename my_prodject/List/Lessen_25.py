# метод insert
# list = ['Anders', 'Gvido', 'Roman', 'Timur']
# list.insert(-2,'Привет')
#
# print(list)

# метод index

# list = ['Anders', 'Gvido', 'Roman', 'Timur']
# print(list.index('Gvido', 0,3))

# метод remove

# food = ['Рис', 'Курица', 'Рыба', 'Брокколи', 'Рис']
# try:
#     food.remove('Ра')
#     print(food)
# except ValueError:
#     print('Нету')

# метод pop
# food = ['Рис', 'Курица', 'Рыба', 'Брокколи', 'Рис']
# del_pop = food.pop()
# print(del_pop)
# print(food)
# # без индекса
# food = ['Рис', 'Курица', 'Рыба', 'Брокколи', 'Рис']
# del_pop = food.pop()
# print(del_pop)
# print(food)
# индекс который выходит за пределы списка
# food = ['Рис', 'Курица', 'Рыба', 'Брокколи', 'Рис']
# del_pop = food.pop(6)
# print(del_pop)
# print(food)