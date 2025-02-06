from open_file.City_game.cities import *


'''
Достал из сити только города и преобразовал их в сет
'''
my_set = {city['name'] for city in cities} # новый вариант
copy_my_set = my_set.copy()
copy_list_set = list(copy_my_set)


bots = copy_my_set.pop() # рандом слово от бота
print(f'Слова бота: {bots}')

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

bools = False

while not bools:
    user_input = input('Введите название города:').strip()
    if user_input == 'Стоп':
        print('Cтоп игра')
        break
    user_city = set(user_input.split(',')) # приобразовка в сет
    out = user_city.intersection(copy_my_set) # сравнение


    if not out:
        print('Такого города нет выиграл бот ')
        break

    str_out = ''.join(out)
    if str_out[0].lower() != bots[-1].lower():
        print(f'Не правильный ответ он должен начинаться на букву {bots[0]}')
        continue
    else:
        print(f'Бот: мне на букву {str_out[-1]}')
        dels = out.pop() # удаляет и возвращает его
        copy_my_set.remove(dels) # окончательно удаляет

        print(f'Удаляю этот город {dels}')
        print(len(copy_my_set))

    for i in copy_list_set:
        if i[0].lower() == str_out[-1]: # Если 1 буква бота равна последней буквы игрока
            bots = i
            copy_list_set.remove(i) # Удаляем слово из городов
            print(f'Бот : {i} , тебе на букву {i[-1]}')
            break

    # else:
    #     print(f'Боту на букву {str_out[-1]}: {}')

    # if out:
    #     print(f"Есть такой город: {str_out}")
    #     dels = out.pop() # удаляет и возвращает его
    #     copy_my_set.remove(dels) # окончательно удаляет
    #     print(f'Удаляю этот город {dels}')
    #     print(copy_my_set)

    # else:
    #     print('Такого города нет')
else:
    bools = True
    print('Ты выиграл')
