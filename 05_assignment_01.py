import datetime


nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None]
]
return_list = []


def decor_flat_generator(func):

    def new_func(*args, **kwargs):
        result = func(*args, **kwargs)
        tm = datetime.datetime.now()
        tm_str = tm.isoformat(sep=' ')[:19]
        return_list.append(tm_str)  # создание строки с временем вызова функции
        func_name = func.__name__
        return_list.append(func_name)  # создание строки с именем функции
        #print(result)
        return_list.append(result)
        # return_list.append(', '.join(map(str, result)))  # создание строки с return для последующей записи в файл
        # создание строки с аргументами (*args) для последующей записи в файл
        return_list.append(', '.join(map(str, args)))
        # создание строки с именнованными аргументами (**kwargs) для последующей записи в файл
        return_list.append(', '.join(map(str, kwargs)))
        print(return_list)
        with open('logger.txt', 'a') as file:
            for line in return_list:
                file.write(f'{line}\n')
        return_list.clear()
        return result
    return new_func


@decor_flat_generator
def flat_generator(iter_list):
    unpacked_list = []
    for inner_list in iter_list:
        for el in inner_list:
            unpacked_list.append(el)
    return unpacked_list


# @decor_flat_generator
# def summator(x, y):
#    return x + y
#
# three = summator(1, 2)
# five = summator(2, 3)
#
# result_1 = summator(three, five)
#
# print('result: ', result_1)
# print('result type: ', type(result_1))
flat_generator(nested_list)

