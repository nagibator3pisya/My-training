#декораторы
# синтаксис

# def my_decorator(func):
#     def wrapper():
#         print(f'Дополнительное поведение до вызова {func.__name__}')
#         func()
#         print(f'Дополнительное поведение полсе вызова  {func.__name__}')
#
#     return wrapper
#
#
# @my_decorator
# def hello_func():
#    print('Helllo')


# def decorator(func):
#     def wrapper():
#         original_result = func()
#         modific = original_result.upper()
#         return modific
#     return wrapper
#
#
#
# @decorator
# def hello_func():
#    return 'Helllo'

# два декоратора
# def html_tag(func):
#     def wrapper():
#         return f'<strong>{func()}</strong>'
#     return wrapper
#
# def html_tag2(func):
#     def wrapper():
#         return f'<b>{func()}</b>'
#     return wrapper
#
# @html_tag
# @html_tag2
# def fincion():
#     return 'Hello'





if __name__ == '__main__':
    # print(hello_func())
    # альтернатива
    # hello_funcs = my_decorator(hello_func)
    # print(hello_funcs())
    # hello_func()
    # print(hello_func())
    # print(fincion())