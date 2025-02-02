# with open('Tests.txt' ,'w', encoding='utf8') as f:
#         f.write('тест\n')
#
# print('Файл создан')


# запись списка, обновить
# lines = ["1\n", "2\n", "3\n"]
# with open('Tests.txt' ,'a', encoding='utf8') as f:
#         f.writelines(lines)
#
# print('Cписок внесен')


# чтение файла
# with open('Tests.txt' ,'r', encoding='utf8') as f:
#         for i in f:
#           print(i,end='')

# прочитать весь файл

# with open('Tests.txt' ,'r', encoding='utf8') as f:
#         contex = f.read()
#         print(contex)


'''
дополнение
'''
# подсчет кол-во строк
# count = 0
# with open('Tests.txt' ,'r', encoding='utf8') as f:
#         for i in f:
#                 count += 1
#                 print(i, end='')
# print(f'{count} - кол-во строк ')


# поиск в слова
t = '5'
with open('Tests.txt', 'r', encoding='utf8') as f:
    for i in f:
        if t in i:
           print(i)
