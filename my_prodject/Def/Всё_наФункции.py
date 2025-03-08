# # замыкание
#
# def hello_user(name: str) -> str:
#     def out_user():
#         print(f'Hello {name}')
#
#     return out_user
#
#
# f = hello_user('Test')
# f()


# Глобальная область видимости

# candy = 5
#
# def get_candy():
#     global  candy
#     candy += 1
#     print(f"{candy}")
#
# get_candy()
# get_candy()
# print(f" Это вызов candy у которого было 5 значение сейчас : {candy}")

# Нелокальная область видимости

x = 0  #глобальная


def outer():
    # внешняя
    x = 1# локальная

    def inner():
        nonlocal x
        # внутрення
        x = 2 # тоже локальная
        print(f"inner({x}) ")

    inner()
    print(f"outer({x}) ")


outer()
print(f"global {x} ")











