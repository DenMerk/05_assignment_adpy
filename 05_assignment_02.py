import datetime
import os

nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None]
]
return_list = []
file_name = "logger_new.txt"
path = os.path.join(os.getcwd(), file_name)


def decor_flat_generator(file_path):
    def _decor_generator(func):
        def new_func(*args, **kwargs):
            tm = datetime.datetime.now()
            tm_str = tm.isoformat(sep=' ')[:19]
            return_list.append(tm_str)  # создание строки с временем вызова функции
            func_name = func.__name__
            return_list.append(func_name)  # создание строки с именем функции
            result = func(*args, **kwargs)
            return_list.append(result)
            # return_list.append(', '.join(map(str, result)))  # создание строки с return для последующей записи в файл
            # создание строки с аргументами (*args) для последующей записи в файл
            return_list.append(', '.join(map(str, args)))
            # создание строки с именнованными аргументами (**kwargs) для последующей записи в файл
            return_list.append(', '.join(map(str, kwargs)))

            with open(file_path, 'a') as file:
                for line in return_list:
                    file.write(f'{line}\n')
            return_list.clear()
            return result
        return new_func
    return _decor_generator


@decor_flat_generator(path)
def flat_generator(iter_list):
    unpacked_list = []
    for inner_list in iter_list:
        for el in inner_list:
            unpacked_list.append(el)
    return unpacked_list


# @decor_flat_generator(path)
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

