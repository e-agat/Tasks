# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

n = int(input())
k = 1
for i in range(1,n+1):
    if i % 2 == 0:
        k = i
        print(k)
