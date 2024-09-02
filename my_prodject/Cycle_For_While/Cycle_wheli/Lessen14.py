# i = 0
# while i < 5:
#     print(i)
#     i += 1
# else:
#     print('Конец')

# i = 0
# while i < 5:
#     if i == 3:
#         print('break')
#         break
#     else:
#         print(i)
#         i += 1
# else:
#     print('Конец')
mult = 1
for i in range(1, 11):
   if i % 2 == 0:
      continue
   if i % 9 == 0:
      break
   mult *= i
print(mult)