from open_file.City_game.cities import *


'''
Достал из сити только города и преобразовал их в сет
'''
my_set = {city['name'] for city in cities} # новый вариант
print(my_set)

'''
это то что я придумал старый
'''
# list = []
# for i in cities:
#     ss = i['name']
#     list.append(ss)
#
# new_set = set(list)
# print(new_set)


