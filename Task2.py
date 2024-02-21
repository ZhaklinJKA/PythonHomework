"""
Дана строка чисел от 0 до 9 необходимо создать словарь где в качестве ключа будет цифра,
а в качестве значения количество этих цифр в строке
"""

# numbers = "0139412831055230677798"
# keyy = {}
#
# for i in numbers:
#     if i in keyy:
#         keyy[i] += 1
#     else:
#         keyy [i] = 1
# print(keyy)



numbers = "0139412831055230677798"
dict_num = {}
for i in range(0, 10):
    dict_num[i] = numbers.count(str(i))
print(dict_num)