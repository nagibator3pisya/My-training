from pprint import pprint

from marvel import *

# nested_dict = {
#     'dict1': {'name': 'John', 'age': '27', 'sex': 'Male'},
#     'dict2': {'name': 'Marie', 'age': '22', 'sex': 'Female'}
# }
# print(nested_dict['dict1']['name'])

# for i in nested_dict:
#     print(i)
#
# print()
#
# for i in nested_dict.items():
#     print(i)
#
# print()
# for i in nested_dict.values():
#     print(i)
#
# print()
#
# for k in nested_dict:
#         print(nested_dict[k]['name'])
'''
чтение вложенных словарей
'''
# item = full_dict[1]['title']
# print(item)
# вывод названий всех фильмов
# for i in full_dict:
#     print(full_dict[i]['title'])

# вывод фильмов те кто относиться к 3й фазе
#
# for k in full_dict:
#     if full_dict[k]['stage'] == 'Первая фаза':
#         print(full_dict[k]['title'])

# for k,v in full_dict.items():
#     if v['stage'] in ['Первая фаза','Вторая фаза']:
#         print(v['title'])

# user = input()
# lists = []
#
# for i in full_dict.items():
#     if i in int(user):
#         lists.append(i)

# print(lists)
# user = int(input())

# for i in full_dict:
#     print(full_dict[i]['title'])

# for id_film,info_film in full_dict.items():
#     if info_film['stage'] in ['Первая фаза']:
#         print(f'id {id_film}')
#         print(f'title {info_film['title']}')
#         print(f'year {info_film['year']}')
#         print(f'producer {info_film['producer']}')
#         print(f'stage {info_film['stage']}')

# user = input()
#
# for k_film,v_film in full_dict.items():
#     if user == v_film['title']:
#         print(f'title {v_film['title']}')
#         print(f'year {v_film['year']}')
#         print(f'producer {v_film['producer']}')
#         print(f'stage {v_film['stage']}')


# new_employees = {
#     "jswift@email.com": {
#         "first_name": "Jane",
#         "last_name": "Swift",
#         "address": {
#             "city": "Boston",
#             "street": "25th Street",
#             "house_number": 25
#         }
#     },
#     "pjohnson@email.com": {
#         "first_name": "Patrick",
#         "last_name": "Johnson",
#         "address": {
#             "city": "Miami",
#             "street": "50th Street",
#             "house_number": 50
#         }
#     }
# }

# for emp_email, emp_info in new_employees.items():
#     print(f'Email {emp_email}')
#     for key in emp_info:
#         if type(emp_info[key]) is dict:
#             print(f'{key}')
#             for sub_k,sub_v in emp_info[key].items():
#                 print(f"\t{sub_k} :{sub_v}")
#         else:
#             print(f"{key}: {emp_info[key]}")

