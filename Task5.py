# 5) Реализуйте алгоритм перемешивания списка.

import random

test_list = [1,2,3,4,5]
print('Тестовый список: ', test_list)

n = len(test_list)

for i in range(n):
    j = random.randint(0, n-1)
    element = test_list.pop(j)
    test_list.append(element)
print('Перемешанный список: ', test_list)

