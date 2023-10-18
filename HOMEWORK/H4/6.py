denga = int(input("Введите деньгу"))
while denga % 2 == 0:
    denga_1 = denga // 2
    print("Гони деньги: ", denga_1)
    denga = int(input("Введите деньгу"))
print(denga * 0.9)