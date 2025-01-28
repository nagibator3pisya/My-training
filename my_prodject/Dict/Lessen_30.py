# from pprint import pprint
#
# from marvel import *
#
# # nested_dict = {
# #     'dict1': {'name': 'John', 'age': '27', 'sex': 'Male'},
# #     'dict2': {'name': 'Marie', 'age': '22', 'sex': 'Female'}
# # }
# # print(nested_dict['dict1']['name'])
#
# # for i in nested_dict:
# #     print(i)
# #
# # print()
# #
# # for i in nested_dict.items():
# #     print(i)
# #
# # print()
# # for i in nested_dict.values():
# #     print(i)
# #
# # print()
# #
# # for k in nested_dict:
# #         print(nested_dict[k]['name'])
# '''
# чтение вложенных словарей
# '''
# # item = full_dict[1]['title']
# # print(item)
# # вывод названий всех фильмов
# # for i in full_dict:
# #     print(full_dict[i]['title'])
#
# # вывод фильмов те кто относиться к 3й фазе
# #
# # for k in full_dict:
# #     if full_dict[k]['stage'] == 'Первая фаза':
# #         print(full_dict[k]['title'])
#
# # for k,v in full_dict.items():
# #     if v['stage'] in ['Первая фаза','Вторая фаза']:
# #         print(v['title'])
#
# # user = input()
# # lists = []
# #
# # for i in full_dict.items():
# #     if i in int(user):
# #         lists.append(i)
#
# # print(lists)
# # user = int(input())
#
# # for i in full_dict:
# #     print(full_dict[i]['title'])
#
# # for id_film,info_film in full_dict.items():
# #     if info_film['stage'] in ['Первая фаза']:
# #         print(f'id {id_film}')
# #         print(f'title {info_film['title']}')
# #         print(f'year {info_film['year']}')
# #         print(f'producer {info_film['producer']}')
# #         print(f'stage {info_film['stage']}')
#
# # user = input()
# #
# # for k_film,v_film in full_dict.items():
# #     if user == v_film['title']:
# #         print(f'title {v_film['title']}')
# #         print(f'year {v_film['year']}')
# #         print(f'producer {v_film['producer']}')
# #         print(f'stage {v_film['stage']}')
#
#
# # new_employees = {
# #     "jswift@email.com": {
# #         "first_name": "Jane",
# #         "last_name": "Swift",
# #         "address": {
# #             "city": "Boston",
# #             "street": "25th Street",
# #             "house_number": 25
# #         }
# #     },
# #     "pjohnson@email.com": {
# #         "first_name": "Patrick",
# #         "last_name": "Johnson",
# #         "address": {
# #             "city": "Miami",
# #             "street": "50th Street",
# #             "house_number": 50
# #         }
# #     }
# # }
#
# # for emp_email, emp_info in new_employees.items():
# #     print(f'Email {emp_email}')
# #     for key in emp_info:
# #         if type(emp_info[key]) is dict:
# #             print(f'{key}')
# #             for sub_k,sub_v in emp_info[key].items():
# #                 print(f"\t{sub_k} :{sub_v}")
# #         else:
# #             print(f"{key}: {emp_info[key]}")
#
# # employees = {
# #     "emp1": {
# #         "id": 1,
# #         "first_name": "Jane",
# #         "last_name": "Swift",
# #         "address": {
# #             "city": "Boston",
# #             "street": "25th Street",
# #             "house_number": 25
# #         }
# #     },
# #     "emp2": {
# #         "id": 2,
# #         "first_name": "Patrick",
# #         "last_name": "Johnson",
# #         "address": {
# #             "city": "Miami",
# #             "street": "50th Street",
# #             "house_number": 50
# #         }
# #     },
# #     "emp3": {
# #         "id": 3,
# #         "first_name": "Alice",
# #         "last_name": "Smith",
# #         "address": {
# #             "city": "New York",
# #             "street": "42nd Street",
# #             "house_number": 42
# #         }
# #     }
# # }
#
# # print(employees.get('emp3'))
#
# # for key_info,value_info in employees.items():
# #     print(f'ключ {key_info}')
# #     for value_infos,deteil in value_info.items():
# #         print(value_infos,deteil.)
#
# dicts = {
#     "Profile": {
#         "id": 3,
#         "first_name": "Alice",
#         "last_name": "Smith",
#         "address": {
#             "city": "New York",
#             "street": "42nd Street",
#             "house_number": 42
#         }
#     }
# }
# # for profile,val in dicts.items():
# #     for profile_d in val:
# #         if type(val[profile_d]) is dict:
# #             print(f'{profile_d}:')
# #             for deteil in val[profile_d]:
# #                 print(f'\t{deteil} = {val[profile_d][deteil]}')
# #         else:
# #             print(f'{profile_d} = {val[profile_d]} ')
#

# Доступ по элементам

dict_sample = {
  "Company": "Toyota",
  "model": "Premio",
  "year": 2012
}
# print(dict_sample.get('Company')) # по ключу
# print(f'Компания: {dict_sample['Company']}')

# Добавление элементов
#
# dict_sample["Capacity"] = "1800CC"
# print(dict_sample)

# Обновление элементов

# dict_sample['year'] = 2014
# print(dict_sample)

# удаление элементов

# del dict_sample["year"]
# print(dict_sample)


# films_2 = {
#     'Мстители: Династия Канга': {
#         'Дата выхода': 2026,
#         'Режиссёр': 'Дестин Дэниел Креттон',
#         'Актёры': ['Бри Ларсон', 'Том Хиддлстон', 'Сэмюэл Л. Джексон', 'Бенедикт Вонг', 'Тильда Суинтон']
#     },
#     'Мстители': {
#         'Дата выхода': 2012,
#         'Режиссёр': 'Джосс Уидон',
#         'Актёры': ['Роберт Дауни мл.', 'Крис Эванс', 'Крис Хемсворт', 'Скарлетт Йоханссон', 'Джереми Реннер']
#
#     }}

# for k,v in films_2.items():
#     print(f'Фильм: {k}')
#
#
#     for deteil_k,deteil_v in v.items():
#         if isinstance(deteil_v, list):
#             print(f"{deteil_k}:")
#             for item in deteil_v:
#                 print(f'\t-{item}')
#         else:
#
#             print(f'{deteil_k}: {deteil_v}')
#     print()


# Обработка других типов в словаре

films_2 = {
    'Мстители: Династия Канга': {
        'Дата выхода': 2026,
        'Режиссёр': 'Дестин Дэниел Креттон',
        'Актёры': ['Бри Ларсон', 'Том Хиддлстон', 'Сэмюэл Л. Джексон', 'Бенедикт Вонг', 'Тильда Суинтон'],
        'Производство': {
            'Студия': 'Marvel Studios',
            'Бюджет': '200 миллионов долларов'
        },
        'Жанры': ('фантастика', 'боевик', 'приключения')
    },
    'Мстители': {
        'Дата выхода': 2012,
        'Режиссёр': 'Джосс Уидон',
        'Актёры': ['Роберт Дауни мл.', 'Крис Эванс', 'Крис Хемсворт', 'Скарлетт Йоханссон', 'Джереми Реннер'],
        'Производство': {
            'Студия': 'Marvel Studios',
            'Бюджет': '220 миллионов долларов'
        },
        'Жанры': ('фантастика', 'боевик', 'приключения')
    }
}

for k,v in films_2.items():
    print(f'Фильм: {k}')


    for deteil_k,deteil_v in v.items():
        if isinstance(deteil_v, list):
            print(f"{deteil_k}:")
            for item in deteil_v:
                print(f'\t-{item}')

        elif isinstance(deteil_v, dict):
            print(f"{deteil_k}:")
            for item in deteil_v:
                print(f'\t{item}')

        elif isinstance(deteil_v, tuple):
            print(f"{deteil_k}:")
            for item in deteil_v:
                print(f'\t{item}')
        else:

            print(f'{deteil_k}: {deteil_v}')
    print()


'''
тема
Генератор словарей
'''