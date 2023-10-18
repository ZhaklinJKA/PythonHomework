spisok_igr = []
nachalo = input("Введите игру: ")
while nachalo != "0":
    if nachalo not in spisok_igr:
        spisok_igr.append(nachalo)

    else:
        print("Игра уже есть в списке")
    nachalo = input("Введите игру: ")
# spisok_igr.sort()
# print(spisok_igr)
print(sorted(spisok_igr))
