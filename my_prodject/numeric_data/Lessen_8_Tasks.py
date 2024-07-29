# d1, d2, d3, d4, d5 = int(input()), int(input()), int(input()), int(input()), int(input())
# num1 = max(d1,d2,d3,d4,d5)
# num2 = min(d1,d2,d3,d4,d5)
#
# print(f'Наибольшее число = {num1}\nНаименьшее число = {num2}')

# упорядочить числа

# num1,num2,num3 = int(input()),int(input()),int(input())
# maxc = max(num1,num2,num3)
# mins = min(num1,num2,num3)
# sort1 = num1 + num2 + num3 - (mins - maxc)
# print(mins,sort1,maxc, sep='\n')


#  Абсолютная сумма
#
# a1 = float(input())
# a2 = float(input())
# a3 = float(input())
# a4 = float(input())
# a5 = float(input())
# print(abs(a1) + abs(a2) + abs(a3) + abs(a4) +abs(a5))

# манхэттенское расстояние

p1 = float(input())
p2 = float(input())
q1 = float(input())
q2 = float(input())

sum = abs(p1 - q1) + abs(p2 - q2)
print(round(sum))