# num = int(input())
#
# for i in range(num+1):
#     kv = i ** 2
#     print(f'Квадрат числа {i} равен {kv}')



# num = int(input())
#
# for i in range(num):
#     kv = (num - i) * '*'
#     print(kv)

m = float(input()) # стартовое количество организмов;
p = float(input()) # среднесуточное увеличение в %;
n = int(input()) #  количество дней для размножения.

for i in range(n):
  print(i + 1,m)
  m = m + m * (p / 100)
