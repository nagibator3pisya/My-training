""""
Дополните приведенный код, используя списочное выражение так, чтобы 
получить новый список, содержащий строки исходного списка, 
где у каждой строки удалён первый символ.
"""""

keywords = ['False', 'True', 'None', 'and', 'with',
            'as', 'assert', 'break', 'class', 'continue',
            'def', 'del', 'elif', 'else', 'except',
            'finally', 'try', 'for', 'from', 'global', 'if',
            'import', 'in', 'is', 'lambda', 'nonlocal', 'not',
            'or', 'pass', 'raise', 'return', 'while', 'yield']

new_keywords = [x[1::] for x in keywords]

print(new_keywords)