''''
На вход программе подаётся строка текста, содержащая целые числа. Напишите программу, 
использующую списочное выражение, которая выведет квадраты чётных чисел, кроме тех квадратов, 
которые оканчиваются на цифру 4
'''''
num = [int(i) for i in input() if i % 2 == 0]
filter = []
print(num)


