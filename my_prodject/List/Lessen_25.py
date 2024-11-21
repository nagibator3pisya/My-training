# Количество артиклей


text = input().lower().split()
count = 0
for i in text:
    if i in ['a', 'an', 'the']:
        count += 1
print(count)






