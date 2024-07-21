# num = int(input())
#
# if -1 < num < 17:
#     print('Принадлежит')
# else:
#     print('Не принадлежит')
#


# num = int(input())
#
# if num <= -1 or num >= 7:
#     print('Принадлежит')
# else:
#     print('Не принадлежит')


# num = int(input())
#
# if -30 < num <= -2 or 7 < num <=25 :
#     print('Принадлежит')
# else:
#     print('Не принадлежит')

# Не выражденный треугольник
#
# a = int(input())
# b = int(input())
# c = int(input())
#
# if a + b > c and a + c > b and b + c > a:
#     print('YES')
# else:
#     print('NO')

# Высокосный год

# god = int(input())
#
# if (god % 4 == 0 and god % 100 != 0) or god % 400 == 0:
#     print('YES')
# else:
#     print('NO')

# Ход ладьи
# x1 = int(input())
# x2 = int(input())
# y1 = int(input())
# y2 = int(input())
#
# if x1 == y1 or x2 == y2:
#     print('YES')
# else:
#     print('NO')


# ход короля

x1 = int(input())
x2 = int(input())
y1 = int(input())
y2 = int(input())

if (x1 == y1) <= 1 or (x2 == y2) <=1:
    print('YES')
else:
    print('NO')