# age = int(input('Cколько вам лет: '))
# if not (age < 12):
#     print('Доступ разрешен')
#
# else:
#     print('Допступ запрещен')


a = int(input())

if a >= 2 and a <= 17:
    b = 3
    p = a * a + b * b
else:
    b = 5

p = (a + b) * (a + b)
print(p)