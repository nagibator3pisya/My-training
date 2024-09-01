# text = input()
#
# while text != 'КОНЕЦ':
#     print(text)
#     text = input()

# text = input()
# sum = 0
# while text != 'стоп' and text != 'хватит' and text != 'достаточно':
#
#     sum += 1
#     text = input()
#
# print(sum)

# sum = int(input())
#
# while sum % 7 == 0:
#     print(sum)
#     sum = int(input())
#
# # тоже самое задание
# num = int(input())
# stock = ""
# while num % 7 == 0:
#     stock += str(num) + "\n"
#     num = int(input())
# print(stock)

# integer = int(input())
# sum = 0
#
# while integer >= 0:
#     sum += integer
#     integer = int(input())
#
# print(sum)


#
# integer = int(input())
# sum = 0
#
# while 1 <= integer <= 5:
#     if integer == 5:
#         sum += 1
#     integer = int(input())
#
# print(sum)



n = int(input())
total = 0

while n != 0:
    if n >= 25:
        n -= 25
        total += 1
    elif n >= 10:
        n -= 10
        total += 1
    elif n >= 5:
        n -= 5
        total += 1
    elif n >= 1:
        n -= 1
        total += 1

print( total)










