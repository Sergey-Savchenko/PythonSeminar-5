# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.

# *Пример:*

# 2 2
#     4

def sum(a,b):
    if b>0:
        return sum(a,(b-1))+1
    if b==0:
        return a

numb1 = int(input('Введите первое число: '))
numb2 = int(input('Введите второе число: '))
print(f"Суммой чисел {numb1} и {numb2} является: {sum(numb1,numb2)}")