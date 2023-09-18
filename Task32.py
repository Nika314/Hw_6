'''Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
 (т.е. не меньше заданного минимума и не больше заданного максимума). Список можно задавать рандомно

На входе : [ 1, 5, 88, 100, 2, -4]
33
200
Ответ: [2, 3]'''


def find_index(arr, min_val, max_val):
    indexes = []
    for i in range(len(arr)):
        if min_val <= arr[i] <= max_val:
            indexes.append(i)
    return indexes
array = [10, 5, 11, 100, 25, 30, 54, 45, 23, 18, 21]
result = find_index(array, 10, 20)
print(result)