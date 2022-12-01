#1
# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму
# элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
 
some_list = [2, 4, 5, 6, 8, 8, 5, 1]
sum = 0
for i in range(len(some_list)):
    if (i % 2 != 0):
        sum += some_list[i]
print(sum)

#2
# Напишите программу, которая найдёт произведение пар чисел списка. Парой 
# считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]
 
 
some_list = [2, 3, 4, 2, 6, 1]
half_len_of_list = int(len(some_list) // 2)
multiple = 1
index1 = -len(some_list)
index2 = len(some_list) - 1
result_list = []
for i in range(half_len_of_list):
    multiple = some_list[index1] * some_list[index2]
    result_list.append(multiple)
    index1 += 1
    index2 -= 1
print(result_list)
 
#3
""" Задайте список из вещественных чисел. Напишите программу, которая найдёт
разницу между максимальным и минимальным значением дробной части элементов.
Пример:
- [1.1, 1.2, 3.1, 5, 10.01] => 0.19 """

some_list = [1.1, 1.2, 3.1, 5, 10.01]
some_list2 = []

for i in some_list:
    some_list2.append(i % 1)

max_reminder = max(some_list2)
min_reminder = min(some_list2)
result = max_reminder - min_reminder

print (round((result), 2))

#4
""" Напишите программу, которая будет преобразовывать десятичное число в двоичное.
Пример:
- 45 -> 101101
- 3 -> 11
- 2 -> 10 """

num = int(input('Введите число: '))
b = 0
some_list = []
some_str = []
while num != 1:
    b = num / 2
    if b % 1 != 0:
        some_list.append(1)
        num -= 1
        num = num / 2
    else:
        some_list.append(0)
        num = num / 2

some_list.append(1)
some_list.reverse()
for i in some_list:
    some_str.append(i)

print(str(some_str)[1:-1].replace(', ', ''))
