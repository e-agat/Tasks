# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X*
# Пример:*
# 5
# 1 2 3 4 5
# 6
# -> 5

n = int(input('Введите количество элементов в списке: '))
lst = []
for i in range(n):
    a = int(input('Введите элементы списка: '))
    lst.append(a)
x = int(input('Введите число Х: '))
min = abs(x - lst[0])
index = 0
for j in range(n):
    count = abs(x - lst[j])
    if count < min:
        min = count
        index = j
       
print(lst[index])