game = input("Введите game (off-завершить): ")
if game == "game":
    for i in range(3):
        number = int(input("Введите число: "))
        if number == 5:
            print("Вы выиграли билет на концерт!")
            break
while game == 'off':
    break
else:
    print("Игра окончена")
