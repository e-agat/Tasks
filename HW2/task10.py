# ; Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, 
# ; а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть, 
# ; чтобы все монетки были повернуты вверх одной и той же стороной. Выведите минимальное 
# ; количество монет, которые нужно перевернуть

n = int(input())
head = 0
tail = 0

for i in range(n):
    coin = int(input())
    if coin ==0:
        tail += 1
    if coin == 1:
        head += 1
if tail > head:
    print(head)
else:
    print(tail)
