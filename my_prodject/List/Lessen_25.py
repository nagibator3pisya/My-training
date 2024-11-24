

numbers_string = input().split()

for i in range(len(numbers_string)):
    numbers_string[i] = int(numbers_string[i])


b = numbers_string.copy()

numbers_string.sort()
b.sort(reverse=True)

print(*numbers_string)
print(*b)
