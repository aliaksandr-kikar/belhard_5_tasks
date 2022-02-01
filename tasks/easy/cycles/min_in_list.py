"""
ЗАДАНИЕ
--------------------------------------------------------------------------------
Написать функцию, которая принимает список целых чисел и возвращает минимальное

Нельзя пользоваться функциями sorted, list.sort, min, max

ПРИМЕРЫ
--------------------------------------------------------------------------------
min_in_list([1, 2, 3, -2, 3, 5]) -> -2
min_in_list([7, 2, 4, 6, 1, 4]) -> 1
"""


def min_in_list(some_list: list) -> int:
    run = True
    while run:
        run = False
        for index in range(len(some_list) - 1):
            if some_list[index] > some_list[index + 1]:
                some_list[index], some_list[index + 1] = some_list[index + 1], some_list[index]
                run = True
    min_value = some_list[0]
    return min_value


if __name__ == '__main__':
    assert min_in_list([1, -1, 5, 7, -2, 4]) == -2
    print('Решено!')
