# длинна строки
# n = 'Привет'
# print(len(n))

# индексация

# s = 'abcdf'
# for i in range(len(s)):
#     print(f'индекс: {i}, символ {s[i]}')

# s = 'abcdf'
# for i in s:
#     print(f'{i}')
# s = 'abc'
# for i in range(1,len(s)+1):
#     print(s[-i])


# f = input()
# i = input()
# o = input()
#
# for j in [f,i,o]:
#     print(j[0].title(),end='')





# for i in sums:
#     count += int(i)
#
# print(count)


# Цифра 2
#
# str_num = input()
# for i in str_num:
#     if i.isdigit():
#         print('Цифра')
#         break
# else:
#     print('Цифр нет')


# Сколько раз?
# string = input()
# zvezda = 0
# plus = 0
# for i in string:
#     if i.count('*'):
#         zvezda += 1
#     elif i.count('+'):
#         plus += 1
#
# print(f'Символ + встречается {plus} раз')
# print(f'Символ * встречается {zvezda} раз')


#Одинаковые соседи

# string = input()
# count = 0
#
# for i in range(len(string)-1):
#     if string[i] == string[i+1]:
#         count +=1
#
# print(count)

# Гласные и согласные

# string = 'Вдохновение – это умение приводить себя в рабочее состояние!'
# glass = 0
# cogl = 0
#
# glass_1 = 'ауоыиэяюе'
# cogl_1 = 'бвгджзйклмнпрстфхцчшщ'
#
# for i in string:
#     if i in glass_1:
#         glass += 1
#     elif i in cogl_1:
#         cogl += 1
#
# print(f'Количество гласных букв равно {glass}')
# print(f'Количество согласных букв равно {cogl}')

# Преобразование десятичной дроби в двоичную
# t = 2
# s = t % 2  остаток в переменной s
# print(s)


num = int(input())
ostator = 0
sum_ostatka = ''

# for i in range(1,num + 1):
#     s = str(i % 2) + sum_ostatka
#     ostator = s
#     ostator //= 2
#     sum_ostatka = ostator
#
#
#
#
# print(sum_ostatka)

while num > 0:
    ostator = num % 2
    sum_ostatka = str(ostator) + sum_ostatka # добавляем остаток в начало строки
    num //= 2 # Делим на 2, чтобы получить следующий остаток

print(sum_ostatka)