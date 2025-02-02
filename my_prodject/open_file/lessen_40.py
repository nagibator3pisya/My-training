# Работа с файлами
# w - создает файл, если файл такой уже есть то он данные старые стирает а новые добовляет
# with open('Test.txt', 'w', encoding='utf8') as f:
#     f.write('Тест файла2')
#
# print('Файл записан')



# a - добавить что то в файл
# with open('Test.txt', 'a', encoding='utf8') as f:
#     f.write('\nТест файла2')
#
# print('Файл изменен')


# добавить + print
#
# with open('Test.txt', 'a', encoding='utf8') as f:
#     print('\nДобавил',file=f)

# Чтение файла
# with open('Test.txt','r',encoding='utf8') as f:
#     for i in f:
#         print(i)

# with open('Test.txt','r',encoding='utf8') as f:
#    index = f.readlines()
#    print(index)
#    str = index[2]
#    print(str)


# list = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet']
# with open('Test.txt','a',encoding='utf8') as f:
#     for i in list:
#         f.write(f'{i}\n')


# with open('Test.txt','r',encoding='utf8') as f:
#     for i in f:
#         print(i)
# print([l.strip() for l in lines])



'''''
Чтение и запись
'''''


# with open('Test.txt','w+',encoding='utf8') as f:
#     f.write('Запись_чтение\n2\n5')
#
#     c = f.read()
#     print(c)
# lists = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet']
# with open('List_file', 'a', encoding='utf8') as f:
#     f.writelines(lists)
#
# print('файл создан')