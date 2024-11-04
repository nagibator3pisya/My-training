# представление строк в памяти компьютера, ASCII и Unicode
# print(ord('a'))
# print(chr(97))


# работа в паре
# s
# for i in range(26):
#     print(ord(chr(2) + i))
#     # print(chr(ord('A') + i))


# letter = ord(input())

# letters = ord(input())
# while True:
#     letters = ord(input())
#     if letters >= ord('Ё'):
#         print('Будем считать что её нет')
#         continue
#     if letters >= ord('Я'):
#         print('Дальше букв нет так как это последняя')
#         flag = False
#         break
#
#     else:
#
#
#         ss = chr(letters + 1)
#         print(ss)

# flag = True
# letter = ord(input().upper())
# while flag:
#
#     if letter >= ord('ё'):
#         print('Будем считать что её нет')
#         continue
#     if letter >= ord('я'):
#         print('Дальше букв нет')
#         flag = False
#         break
#
#     else:
#         # letter = ord(input().upper())
#         ss = chr(letter + 1)
#
#     print(ss.upper())

# for i in range(ord(letter),ord(letter)):
#     print(i)


# Символы в диапазоне

# ord1 = int(input())
# ord2 = int(input())
#
# for i in range(ord1,ord2+1):
#     print(chr(i),end=' ')

# Простой шифр

# string = input()
#
# for i in string:
#     print(ord(i),end=' ')
#
# s = input()
# for i in range(len(s)):
#     print(ord(s[i]), end = ' ' )

# Самое тяжелое слово
# cnt = 0
# cnt_mx = 0
# word = ''
#
# for i in range(4):
#     s = input()
#     cnt = 0
#     for j in s:
#         cnt += ord(j)
#         if cnt > cnt_mx:
#             cnt_mx = cnt
#             word = s
#
#
# print(word)


# Стоимость ответа
comment = input()
coint  = 0
ss = 0
new_com = 0
for i in range(len(comment)):
    coint += ord(comment[i])
    ss = coint*3
    new_com+=1

print(f"Текст сообщения: '{comment}'\nСтоимость сообщения:{ss}🐝 {new_com}")

# s = ord(comment)
# coint += s
# ss = coint*3
# print(f'{comment}\n{coint}')


# 291 a
# coint = 0
# for i in comment:
#     pr = ord(i)
#     sums = pr * 3
#     print(f'Текст сообщения: {comment}\nСтоимость сообщения:{sums}')















