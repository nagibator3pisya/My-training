# Построчный вывод
# str = 'У лукоморья дуб зеленый златая цепь на дубе том'
# s = str.split()
# print(*s,sep='\n')

# Инициалы
# str = input().split()
#
# # print(string_split) # ['Владимир', 'Семенович', 'Высоцкий']
#
# for i in range(len(str)):
#     s = '.'.join(str[i][0])
#     print(s,end='.')

# Windows OS

# str = input().split('\\')
# # print(str) # ['C:\\Windows\\System32\\calc.exe']
# # print(' '.join(str)) # C:\Windows\System32\calc.exe
# for i in range(len(str)):
#     str_join = '\\'.join(str[i])
#     replse = str_join.replace("\\",'')
#     print(replse)


# Диаграмма

# num = input().split()
#
# for i in range(len(num)):
#     num[i] = int(num[i])
#     print('*' * num[i])


# Корректный ip

# ip_str = input().split('.')
# valid = True # Этот  флаг  будет  хранить  информацию  о  том,  является  ли  IP-адрес  корректным.
# for i in range(len(ip_str)): # перебор части элементов ip
#     numbers = int(ip_str[i]) # преобразуем в число
#     if not( 0 <= numbers <= 256): # Если не в диапозоне то false и перекрываем цикл
#         valid = False
#         break
#
# if valid:
#     print('ДА')
# else:
#     print('НЕТ')

# Добавь разделитель
# str = input()
# simvol = input()
# print(simvol.join(str))

# Количество совпадающих пар
# a = input().split()
# count = 0
# for i in range(len(a)):
#     for j in range(i + 1,len(a)):
#         if a[i] == a[j]:
#             count += 1
#
# print(count)
