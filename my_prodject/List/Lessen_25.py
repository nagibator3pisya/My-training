# Внутренние циклы и внешние циклы в генераторе списков

# a = [(i,j) for i in range(3) for j in range(4)]
#
# print(a)
# [(0, 0), (0, 1), (0, 2), (0, 3),
# (1, 0), (1, 1), (1, 2), (1, 3), (2, 0), (2, 1), (2, 2), (2, 3)]

# a = [(i,j) for i in range(3) if i % 2 == 0 for j in range(4)]
# print(a)

""""
Перевод многомерного массива во однострочный
"""""
# matrix = [
#     [0, 1, 2, 3],
#     [4, 5, 6, 4],
#     [5, 6, 10, 8]
# ]
#
# generator = [x for row in matrix for x in row ]
# print(generator)
