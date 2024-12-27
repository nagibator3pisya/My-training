# numbers = (2, 3, 5, 7, -11, 13, 17, 19, 23, 29, 31, -6, 41, 43, 47, 53, 59, 61, -96, 71, 1000, -1)
'''
Дополните приведенный код так, чтобы он вывел произведение элементов кортежа numbers.
'''


# total = 1
# for i in numbers:
#     total += i
#
# print(total)


'''
Замена  'Санкт-Петербург' на 'москву
'''

# poet_data = ('Пушкин', 1799, 'Санкт-Петербург')
# ss = poet_data[:-1] + ('Москва',)
#
# print(ss)

'''
Дополните приведенный код так, чтобы он вывел список, 
содержащий средние арифметические значения чисел каждого вложенного 
кортежа в заданном кортеже кортежей numbers.
'''
#
# numbers = ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4), (90, 10))
#
#
# new_list = []
#
# for i in numbers:
#     total_sum = sum(i)
#     count_S = len(i)
#     out = total_sum / count_S
#     new_list.append(out)
#
# print(new_list)

'''
Формат входных данных
На вход программе подается натуральное число 
n, далее следует n строк с фамилией школьника и его оценкой на каждой из них.

Формат выходных данных
Программа должна вывести 
сначала все введённые строки с фамилиями и оценками учеников в том же порядке. Затем следует пустая строка, а затем выводятся строки с фамилиями и оценками хорошистов и отличников (в том же порядке).

Примечание 1. Оценка ученика – это натуральное число от 
1 до 5

Примечание 2. Гарантируется, что в классе есть хотя бы один хорошист (обладатель оценки 4)
или отличник (получивший 5).
'''
# number = int(input())
# new_list = []
# for item in range(number):
#     str_usenik = input().split()
#     new_list.append(str_usenik)
#
# out = []
# for item in new_list:
#     if any(int(i) >= 4 for i in item if i.isdigit()): # хотя бы один из элементов будет истинным any
#         out.append(item)
#
# for sublist in new_list: # распоковывать все
#     print(*sublist)
#
# print()
#
# for sublist in out:
#     print(*sublist)

'''
2 решение с картежами
'''
# student = [tuple(input().split()) for _ in range(int(input()))] # [('asdasd', '2'), ('asdasd', '1') ]
#
# for students in student:
#     print(*students)
#
#
# print()
#
# for name,gea in student:
#     if int(gea) > 3:
#         print(name,gea)



"""
Вам пришло секретное послание. Оно содержит много странных символов, которые вы не можете понять.
Но вы знаете, что в этом послании используются только маленькие русские буквы. Используйте знание языка Python
а так же знание for i чтобы расшифровать его.
"""
# # Секретное послание
# secret_letter = [['DFВsjl24sfFFяВАДОd24fssflj234'], ['asdfFп234рFFdо24с$#afdFFтasfо'],
# ['оafбasdf%^о^FFжа$#af243ю'],['afпFsfайFтFsfо13н'],
# ['fн13Fа1234де123юsdсsfь'], ['чFFтF#Fsfsdf$$о'],
# ['и$##sfF'], ['вSFSDам'],['пSFоsfнрSDFаSFвSDF$иFFтsfaсSFя'],
# ['FFэasdfтDFsfоasdfFт'], ['FяDSFзFFsыSfкFFf']]
# # Список с маленькими русскими буквами
# small_rus = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и',
# 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф',
# 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
# out = []
# for i in secret_letter:
#     for j in i:
#         ss = ''.join(char for char in j if char in small_rus)
#         out.append(ss)
#
# print(out) # ['я', 'просто', 'обожаю', 'пайтон', 'надеюсь', 'что', 'и', 'вам', 'понравится', 'этот', 'язык']


# tel = input()
# flag = True
# ss = tel.replace('(','').replace(')','').replace('-','').replace(' ','')
# if len(tel) != 11:
#     print(len(ss))
#     flag = False
#     print('1 проверка')
# if not (ss.startswith('8') or ss.startswith('+7')):
#     flag = False
#     print('2 проверка')
# if not ss[1:].isdigit():
#     flag = False
#     print('3 проверка')

tel = input()
flag = True

clear_tel = tel.replace('(','').replace(')','').replace('-','').replace(' ','')
if len(tel) == 11:
    print(len(clear_tel))
    flag = False
    print('1 проверка')

if not (clear_tel.startswith('8') or clear_tel.startswith('+7')):
    flag = False
    print('2 проверка')

if not clear_tel[1:].isdigit():
    flag = False
    print('3 проверка')
#+77053183958
# +77773183958
#
if flag:
    print('Прошли')



'''
+77053183958
+77773183958
87773183958
+(777)73183958
+7(777)-731-83-58
+7(777) 731 83 58
+9(777) 731 83 58
'''





