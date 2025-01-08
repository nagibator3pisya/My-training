# создания словаря,словарь

# d = {}
# dicts = dict()
#
# dd = {'key':'value' , 'key1':'value1'}

'''''
Ключи и значения
'''''

# ddd = {1:'value',
#        'key2':2,
#        (1,2,3):[1,2,3]}
# print(ddd)

'''
dict() - создания в месте с ним
'''
# keys_and_values = [("Александр", 23), ("Виктория",43),
#                    ("Евгений", 26), ("Петр", 52), ("Денис", 32)]
#
# print(dict(keys_and_values))

# ещё один способ создания

# team_names = ["Александр", "Виктория", "Евгений", "Петр", "Денис"]
# dict_team_names = dict.fromkeys(team_names,0)
# print(dict_team_names)





'''
Работа со словарями
'''
class_ = {'name': '11a',
          'students': 20,
          'teacher': 'Ivan Ivanovich'}
# # in
# print('name' in class_)
# # len
# print(len(class_))



# .keys() - получить все ключи словаря
# .values() - получить все значения словаря
# .items() - получить все пары ключ-значение словаря
# перебор словаря
# for o in class_.keys():
#     print(o)

# for o in class_.values():
#     print(o)

# for o in class_.items():
#     print(o)

# for k,v in class_.items():
#     print(k,v)

'''
перевод из словаря в список
'''
# print((list(class_.items())))
# print(type(list(class_.values())))
# print(type(list(class_.values())))

'''
Работа с методами

'''
