phone_number = (input("Введите номер телефона: "))
phone_number_new = phone_number.replace(')', '').replace('(', '').replace(' ', '').replace('-', '')
print(phone_number_new)