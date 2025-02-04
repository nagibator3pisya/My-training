from open_file.City_game.cities import *


'''
Достал из сити только города и преобразовал их в сет
'''
my_set = {city['name'] for city in cities} # новый вариант
copy_my_set = my_set.copy()
count = 0

for i in copy_my_set:
   count += 1
print(f'Количество слов: {count}')

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

bools = True

while bools:
    user_input = input('Введите название города:').strip()
    if user_input == 'Стоп':
        print('Cтоп игра')
        break
    user_city = set(user_input.split(','))
    out = user_city.intersection(copy_my_set)
    if out:
        print(f"Есть такой город: {''.join(out)}")
        print(f'Удаляю этот город {out.pop()}')
        print(copy_my_set)

    else:
        print('Такого города нет')

