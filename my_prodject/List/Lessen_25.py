l = input().split()

for i in range(len(l)):
    l[i] = int(l[i])

min_value = min(l)
max_value = max(l)

min_index = l.index(min_value)
max_index = l.index(max_value)

l[max_index],l[min_index] = min_value,max_value

print(*l)
