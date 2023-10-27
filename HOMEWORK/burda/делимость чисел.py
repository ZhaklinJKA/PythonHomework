num = int(input())
count = 0
for i in range(3, num+1):
    if num % i == 0 and i % 3 == 0:
        count += 1
print(count)
