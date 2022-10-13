# 3) Задайте список из n чисел последовательности (1 + 1/n)^n и выведите на экран их сумму.

# *Пример:*

#     Для n=4 {1: 2, 2: 2.25, 3: 2.37, 4: 2.44}
#     Сумма 9.06

n = int(input('Введите число n: '))

list_numbers = []
list_numbers = [round((1 + 1/n)**n, 2) for n  in range(1,n+1)]
print(list_numbers)
print(sum(list_numbers))








