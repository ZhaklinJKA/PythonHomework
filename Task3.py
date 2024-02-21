"""
Напишите программу принимающую ввод информации о треке(место в чарте,исполнитель, название) пока пользователь
не введет "off". Программа должна вывести всю информацию в виде словаря вида: {(место,испонитель): название трека}
"""

inf_song =dict()
while True:
    place = input('место:').lower()
    if place != 'off':
        singer = input('исполнитель:').lower()
        music = input('песня:').lower()
        inf_song[place,singer] = music
        print(inf_song)
    else:
        print('пока')
        break

