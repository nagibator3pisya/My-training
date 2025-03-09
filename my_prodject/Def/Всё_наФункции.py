# замыкание

# def names():
#     all_name = []
#
#     def inner(name:str)->list:
#         all_name.append(name)
#         return all_name
#     return inner
#
#
# student = names()
# print(student('Петя'))
# print(student('Вася'))
# print(student('Настя'))



# def counter():
#     count = 0
#
#     def inner(value: int)-> int:
#         """
#         nonlocal count: изменяем значение переменной count
#         :param value:
#         :return:
#         """
#         nonlocal count
#         count += value
#         return count
#     return inner
#
# count = counter()
# print(count(1))
# print(count(1))
# print(count(1))


def pow_(base):
    def inner(value):
        return value ** base
    return inner


if __name__ == '__main__':
    pw = pow_(2)
    print(pw(5))
