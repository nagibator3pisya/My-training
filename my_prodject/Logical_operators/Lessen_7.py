# Вид треугольника
#
# a = int(input())
# b = int(input())
# c = int(input())
#
# if a == b and b == c:
#     print('Равносторонний треугольник')
# elif (a == b and a != c) or (a == c and a != b) or (b == c and b != a):
#     print('равнобедренным ')
#
# elif a != b != c:
#     print('Разносторонний ')

# Серединное число

# a = int(input())
# b = int(input())
# c = int(input())
#
# if a < b < c or  a > b > c:
#     print(b)
# elif c < a < b  or c > a > b:
#     print(a)
# else:
#     print(c)

# Количество дней
# month_number = int(input())
#
# if month_number in (1, 3, 5, 7, 8, 10, 12):
#   print(31)
# elif month_number == 2:
#   print(28)
# else:
#   print(30)

ves = int(input())

if ves <= 60:
    print('Легкий вес')
if ves <= 64:
    print('Полусредний вес')
if ves <= 69:
    print('Первый полусредний вес')




