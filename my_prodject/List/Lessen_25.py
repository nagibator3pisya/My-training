''''
Дополните приведенный код списочным выражением, 
чтобы получить новый список, содержащий только слова длиной не менее пяти символов (включительно).
'''''

keywords = ['ll','False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'try', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'while', 'yield']

lengths = [i for i in keywords if len(i) <= 5]

print(lengths)