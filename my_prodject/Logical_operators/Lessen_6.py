age = int(input('Сколько вам лет: '))
grade = int(input('В каком классе вы учитесь?: '))
city = input('В каком городе вы живете?')

if age >= 12 and grade >= 7 and city == 'Донецк':
    print('Доступ разрешен')
else:
    print('Доступ запрещён')



