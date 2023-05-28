def call_menu():
    menu = int(input("Меню:\n 1. добавить контакт\n 2. найти контакт\n 3. изменить контакт\n 4. просмотр всех контактов\n 5. удалить контакт\n 6. удалить все контакты\n 7. выход\n"))
    return menu

def enter_data():
    first_name = input("Введите имя: ")
    patronymic = input("Введите отчество: ")
    last_name = input("Введите фамилию: ")
    date_birthday = input("Введите дату рождения: ")
    phone_number = input("Введите номер телефона: ")
    data_contact = (first_name + " " + patronymic +  " "  + last_name + " " + date_birthday + " " + phone_number + " " + "\n").lower()
    return data_contact

def get_data():
    data_contact = input("Введите данные контакта для поиска: ").lower()
    return data_contact

def get_numberContact():
    number_contact = int(input("Введите номер контакта: "))
    return number_contact
