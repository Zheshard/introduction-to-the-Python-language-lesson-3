# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# Пример:
# 5
#     1 2 3 4 5
#     3
#     -> 1
import random
N = int(input('Ввести количество элементов в массиве: '))
array = []

for i in range(N):
    array.append(random.randint(1,10))

X = int(input('Число, которое нужно найти: '))

count = 0
for i in range(len(array)):
    if X == array[i]:
        count += 1

print(array)
print(f'В массиве число {X} встречается {count} раз')