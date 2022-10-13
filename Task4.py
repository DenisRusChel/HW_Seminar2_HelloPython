# 4) Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях.
# Позиции вводятся с клавиатуры .

n = int(input('Задайте количество элементов N: '))

ran = range(-n, n+1)
list_numbers = list(ran)
print(list_numbers)

a = int(input('Введите позицию первого элемента: '))
b = int(input('Введите позицию второго элемента: '))

result = list_numbers[a-1] * list_numbers[b-1]

print(f'{list_numbers[a-1]} * {list_numbers[b-1]} = {result}')













