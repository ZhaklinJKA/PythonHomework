# assessments = list(map(int, input().split()))
# five = []
# for i in assessments:
#     if i == 5:
#         five.append(i)
# percent = len(five) / len(assessments) * 100
#
# print(percent)

marks = list(input("Введите отметки: ").split())
pyat = marks.count("5")
print(pyat)
g = pyat / len(marks) * 100
print(g)