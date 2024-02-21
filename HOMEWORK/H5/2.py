assessments = list(map(int, input().split()))
assessments_count = [assessments.count(5), assessments.count(4), assessments.count(3)]
percent = sum(assessments_count) / len(assessments) * 100
print(assessments, assessments_count, percent)


# mark = list(input("Введите отметки через пробел: ").split())
# pyat = 0
# chet = 0
# tri = 0
#
# for i in mark:
#     if i == "5":
#         pyat += 1
# print(pyat)
#
# for i in mark:
#     if i == "4":
#         chet += 1
# print(chet)
#
# for i in mark:
#     if i =="3":
#         tri += 1
# print(tri)
# a = (pyat + chet + tri) /len(mark * 100)
# print(a)

mark = list(input("Введите отметки через пробел: ").split())
print(sorted(mark))
print(mark.count("5") + mark.count("4") + mark.count("3") / len(mark) * 100)
