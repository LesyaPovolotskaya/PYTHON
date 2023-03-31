# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)


from random import randint
min = 2
max = 15
data = [randint(1, 10) for _ in range(20)]
print("Массив: ", data, sep='\n')
indexes = [i for i, j in enumerate(data) if min <= j <= max]

