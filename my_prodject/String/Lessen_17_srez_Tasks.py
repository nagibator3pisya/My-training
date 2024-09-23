# s = 'abcdefg'
# print(s[2:5])


# s = 'abcdefg'
# print(s[3:])


# s = 'abcdefg'
# print(s[:3])

# s = 'abcdefg'
# print(s[::-3])


# Проверка на полиндром

# string = input()
# reversed = string[::-1]
#
# if reversed == string:
#     print('YES')
# else:
#     print('NO')

# делаем срезы

# text = input()

# if len(text) > 3:
#     obsee_len = len(text)
#     free_sting = text * 3
#
#
#     one_index = text[0]
#     free_index = text[0:3]
#     free_index_last = text[-3:]
#     string_reversed = text[::-1]
#     string_last_one = text[1:-1]
#     print(obsee_len,free_sting,one_index,free_index,free_index_last,string_reversed,
#           string_last_one, sep='\n')
# else:
#     print('Длинна меньше трех символов')



# Делаем срезы 2
# text = input()
#
#
#
# if len(text) > 5:
#     index_free = text[2]
#     last_index = text[-2:-1]
#     one_five_index = text[:5]
#     whole_string = text[:-2]
#     even_string = text[::2] # четные
#     no_even_string = text[1::2]# не четные
#     string_reversed = text[::-1]
#     obratn_porzd = text[-1::-2]
#     print(index_free,last_index, one_five_index,whole_string,even_string,no_even_string,string_reversed,obratn_porzd,sep='\n')
# else:
#     print('Длинна меньше пяти символов')


# Две половинки
text = 'abcdef'
l = len(text) + 1
part_1 = text[0:l//2]
part_2 = text[l//2:]
ss = part_2 + part_1
print(ss)
