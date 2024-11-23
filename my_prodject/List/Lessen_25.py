# Взлом Братства Стали

text = input()

for i in range(int(text[1:])):
    string = input()
    if '#' in string:
        string = string[:string.find('#')]

    print(string.rstrip())





