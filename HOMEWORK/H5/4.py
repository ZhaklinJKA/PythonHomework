# lastname = input("Фамилия препода")
# work = input("Должность")
# student_all = list(map(int, input().split(sep=","))) #sep= запятую видит и хоп режет
# spisok = []
# spisok.append(lastname)
# spisok.append(work)
# spisok.append(student_all)
# print(spisok)

spisok_all = []
lastname = input("Фамилия препода: ")
work = input("Должность: ")
student_all = input("Введите список учеников: ").split()

spisok_all.append(lastname)
spisok_all.append(work)
spisok_all.append(student_all)
print(spisok_all)

