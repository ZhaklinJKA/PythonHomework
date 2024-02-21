import math #созыв друга-помощника
Sokr = float(input("Введите ширину: "))
height = float(input("Введите высоту: "))
paint_spent = int(input("Введите расход краски: "))
paint_v = int(input("Введите объём банки краски: "))
percent = int(input("Введите процент запаса: "))
s = Sokr * height
required_v = s / paint_spent * (1 + percent / 100)
bottles_number = math.ceil(required_v / paint_v) #округление до большего числа
left = paint_v * bottles_number - required_v
a = round(s, 2)
b = round(required_v, 2)
c = bottles_number
d = round(left, 2)
print(a + "м^2")
print(b + "л")
print(c + "шт")
print(d + "л")