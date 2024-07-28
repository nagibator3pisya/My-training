# вычисление лет собаки
# age_dog = int(input())
# if  age_dog <= 2:
#     n = age_dog * 10.5
#     print(f'Возрост собаки не меньше двух лет {n}')
# elif age_dog >= 2:
#     n2 = (age_dog - 2) * 4 + 21
#     print(n2)

# положительное число
#
# num = float(input())
# out = int(num * 10)
# out2 = out % 10
# print(out2)

#  положительное действительное число. Выведите его дробную часть.
floats = float(input())
integers = ( floats - int(floats) ) % 1

print(integers)