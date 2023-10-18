fio = str(input())
fio_1 = fio.split(' ',2)
surname = fio_1[0]
name = fio_1[1]
patronymic = fio_1[2]
i = name[0]
o = patronymic[0]
print(surname + ' ' + i + '.' + o + '.')
