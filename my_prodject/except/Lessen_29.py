# data_lst = ['1', '2', '3', '4d', 5]
# new_list = []
# for i in data_lst:
#     try:
#         if int(i):
#             new_list.append(i)
#     except ValueError:
#         print(f'Это не число: {str(i)}')
#
#
# print(new_list)

# номер телефона

nums= [
'+77053183958',
'+77773183958',
'7773183958',
'+(777)73183958',
'+7(777)-731-83-58',
'+7(777) 731 83 58']

# phone = ', '.join(nums)
# clear = phone.replace('(','').replace(')','').replace('-','').replace(' ','')
# # print(clear)

# print(nums[1])
# for phones in nums:
#     clear_phones = phones.replace('(','').replace(')','').replace('-','').replace(' ','')
#     try:
#         if not clear_phones.startswith('+7') or clear_phones.startswith('8'):
#             raise ValueError("не +7 и не 8")
#         if len(clear_phones) == 11:
#             raise ValueError("Не прошла проверку длинна")
#         if not clear_phones[1:].isdigit():
#             raise ValueError("не цифры")
#     except ValueError as e:
#         print(f'{e} {phones}')
#
#
# else:
#     print('ok')










