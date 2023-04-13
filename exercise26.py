# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

# Пример:

# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8

def power(a,b):
    if b>0:
        return power(a,b-1)*a
    if b<0:
        return power(a,b+1)/a
    if b==0:
        return 1

numb1 = int(input('Введите число: '))
numb2 = int(input('Введите степень: '))
print(f"Степенью {numb2} числа {numb1} является: {power(numb1,numb2)}")
