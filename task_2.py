# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# Пример:
# 5
#     1 2 3 4 5
#     6
#     -> 5

import random
N = int(input('Ввести количество элементов в массиве: '))
array = []

for i in range(N):
    array.append(random.randint(1,15))

X = int(input('Введите число: '))
difMin = abs(array[0] - X)

for i in range(len(array)):
    dif = abs(array[i] - X)
    if dif <= difMin:
        nearest = array[i]
        difMin = dif

print(array)
print(f'Ближайшее по величене значение заданному числу {X} является число {nearest}')