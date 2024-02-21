first_num = int(input())
second_num = int(input())
third_num = int(input())
sum = first_num+second_num+third_num
if first_num>second_num and first_num>third_num:
    max = first_num
if second_num>first_num and second_num>third_num:
    max = second_num
if third_num>first_num and third_num>second_num:
    max = third_num
if first_num<second_num and first_num<third_num:
    min = first_num
if second_num<first_num and second_num<third_num:
    min = second_num
if third_num<first_num and third_num<second_num:
    min = third_num
print(sum)
print(max)
print(min)