#  Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
# 10 -> 1 2 4 8
       
n = int(input("Введите число n: "))  
x = 1                   
while x <= n:           
    print(x, end=' ')  
    x *= 2             


