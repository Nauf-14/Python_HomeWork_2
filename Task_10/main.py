# На столе лежат n монеток.Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть,
# чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть. Input: 5 -> 1 0 1 1 0  Output:2

n = int(input("Введите кол-во монет: "))
count1 = 0
count2 = 0
head_coin = 1
tail_coin = 0
min_number_of_turns = 0
for i in range(n):
    x = int(input("Введите цифру ,соответствующию стороне монеты: "))
    if x == 1:
        count1 += 1       
    elif x == 0:
        count2 += 1

if count1 > count2 and count1 != count2:
        if min_number_of_turns < count2:
            min_number_of_turns = count2
        
elif count1 < count2 and count1 != count2:
        if min_number_of_turns < count1:
            min_number_of_turns = count1
print(min_number_of_turns)




