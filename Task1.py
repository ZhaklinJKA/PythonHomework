"""
Создайте словарь, в котором ключами будут числа от 1 до 10, а значениями эти же числа, возведенные в куб.
"""
numbers = dict()
for i in range(1, 11):
    numbers[i]= i**3 #без i низя, так как тогда он по умолчанию считает, но не выводит их всех, ибо цикл усе на 10

print(numbers)