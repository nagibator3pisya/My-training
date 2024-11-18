"""""
Дополните приведённый ниже код, чтобы он:

Заменил второй (по порядку) элемент списка на 17;
Добавил числа 4, 5 и 6 в конец списка;
Удалил первый (по порядку) элемент списка;
Удвоил список;
Вставил число 25 по индексу 3;
Вывел список с помощью функции print()

"""""

numbers = [8, 9, 10, 11]
copy_list = numbers.copy()


zamena = copy_list[1] = 17
print(copy_list, sep='\n')

new_list = [4,5,6]
insert_list = copy_list.extend(new_list)
print(copy_list)

del copy_list[0]

print(copy_list)

ss = copy_list * 2
print(ss)

vctavka = copy_list.insert(3,25)

print(copy_list)

print(copy_list)



