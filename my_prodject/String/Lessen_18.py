# Методы строк
from collections import Counter

#
# s = 'foO BaR BAZ quX'
# print(s.capitalize())
# # Foo bar baz qux

# s = 'foO BaR BAZ quX'
# print(s.upper())

# Заглавные буквы
# text = 'Chris Alan'
#
# if not text.istitle():
#     print("NO")
# else:
#     print('YES')

# Хороший оттенок, поиск подстроки хорош
# text = input().lower
# if 'хорош' in text:
#     print("YES")
# else:
#     print('NO')

# text = input()
# count = 0
# for i in text:
#     if i.islower():
#         count += 1
#
# print(count)


# startswith
# a = 'Mushroooom soup'
# print(a.startswith('us',1,3))

#endswith
# a = 'Mushroooom soup'
# print(a.endswith('p'))
# print(a.endswith('up'))
# print(a.endswith('up'))


#find

# s = 'one true false bas'
#
# print(s.rfind('bas'))

# strip

# s ='        Привет'
# print(s.strip())

# lstrip

# s ='-----Bee-----'
# print(s.lstrip('-'))


# replace

# s = 'foo bar foo baz foo qux'
# print(s.replace('foo','dd',1))

# количество слов
# s = 'In 2010, someone paid 10k Bitcoin for two pizzas.'
# print(s.count(" ") + 1) # 1 вариант то есть count считает до пробела +
# # следующее слово, если слово одно, то пробела нет, и получаем +1, то есть 1 слово
# print(len(s.split())) # split разбивает строку на отдельные слова, а len подсчитывает


# Минутка генетики
# s = 'аааГГЦЦцТТттт'.lower()
# print(s)
# print('Аденин:', s.count('а'))    # выводим результаты для каждой буквы
# print('Гуанин:', s.count('г'))
# print('Цитозин:', s.count('ц'))
# print('Тимин:', s.count('т'))

# # 2 варинт
# s = input().upper()
# for i in ('Аденин','Гуанин','Цитозин','Тимин'):
#     print(i,s.count(i[0]))

# # Очень странные дела
#
# n = int(input())
# count = 0
# for i in range(n):
#     n = input()
#     if n.count('11') >= 3:
#         count += 1
#
# print(count)


# Количество цифр

# str = input()
# counter = 0
#
# for i in str:
#     if i.isdigit():
#         counter += 1
#
# print(counter)

# 2 й вариант в виде другого цикла
# str = input()
# counter = 0
# i = 0
# while i < len(str):
#     if str[i].isdigit():
#         counter += 1
#     i += 1
#
# print(counter)


# Задача .com or .ru


# if s in ['.com','.or']:
#     print('YES')
# else:
#     print('NO')
# s = input()
# if s.endswith('.com') or s.endswith('.ru'):  # Проверяем, заканчивается ли строка на ".com" или ".ru"
#     print('YES')
# else:
#     print('NO')


# Самый частотный символ

# string = 'aaaabbc'.lower()
#
# char_counter = Counter(string)
# # most_common[n] - возвращает наиболее повторяющиеся элементов, что бы не выводить их все
# # [0][0] первый элемент списка и первый элемент картежа
# # если без них  [('a', 4)] буквы а встречатся 4 раза, [0] - ('a', 4) 1 список кортежа
# # 2 й [0] первый элемент списка
# most = char_counter.most_common(1)
# print(most)

# s = 'aaabb'
# x = 0
# y = ''
#
# for i in range(len(s)):
#     if s.count(s[i]) >= x:
#         x = s.count(s[i])
#         y = s[i]
#
# print(x,y)

# # Первое  и последнее вхождение
# s = 'abcdefgf'
# first_index = s.rfind('f')
# last_index = s.find('f')
#
# if first_index != -1: # -1 возвращает если строка не найдена
#     if first_index == last_index: # если в конце и в начале индексы совпадают,то подстрака встречается 1 раз
#         print(first_index)
#     else:
#         print(first_index, last_index)
#
# else:
#     print('NO')

## Удаление фрагмента
# s = input()
#
# a = s.find('h')
# b = s.rfind('h')+1
#
# print(s[:a], s[b::],sep='')

# s1 = ''
# print(s1.isspace())
# Плохие комментарии
# n = int(input())
# for i in range(1,n+1):
#     n = input()
#     if len(n) == 0 or n.isspace():
#         print(f'{i}: COMMENT SHOULD BE DELETED',sep='\n')
#     else:
#         print(f'{i}: {n}')

# Автомобильный номер
# isalpha буква,
# number = input()
#
# # изначально номер не коррктный
# is_valid = 'NO'
#
# # допустимые буквы для автомобильного номера
# allowed_letters = 'АВЕКМНОРСТУХ'
# # А123ВС_45
# if 9 <= len(number) <= 10:
#     letters = number[0] + number[4:6]
#     digget = number[1:4] + number[8:]
#     underline = number[6]
#
#     # проверка на то что в номере еть цифры и нижнее подчеркивание
#     if  digget.isdigit() and underline == '_':
#         is_valid = 'YES'
#
#
#
#     # Проверка на то что все буквы являются, допустимы
#
#     for i in letters:
#         if i not in allowed_letters:
#             is_valid = 'NO'
#
# print(is_valid)



user_name = input()

is_valid = "Correct"

# Проверяем, начинается ли никнейм с символа @
if not user_name.startswith("@"):
    is_valid = "Incorrect"

# Проверяем длину никнейма
elif not (5 <= len(user_name) <= 15):
    is_valid = "Incorrect"

# Проверяем, состоит ли никнейм из строчных букв и цифр (кроме первого символа)
elif not user_name[1:].isalnum():
    is_valid = "Incorrect"

# Проверяем,  все ли буквы в никнейме строчные
elif user_name[1:] != user_name[1:].lower():  #  Сравниваем с версией в нижнем регистре
    is_valid = "Incorrect"

print(is_valid)










# # if min_name >= len(user_name) <= max_name:
# if user_name.startswith('@') or user_name.isalnum():
#     digget = min_name <= len(user_name) <= max_name
#
#
#
# else:
#     is_valid = 'Incorrect'
#
# print(is_valid)














