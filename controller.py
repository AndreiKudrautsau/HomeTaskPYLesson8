import view
import database

def menu():
    while True:
        choice = view.call_menu()
        print(f"Ваш выбор: {choice}")
        if choice == 1:
            data_contact = view.enter_data()
            database.enter_data(data_contact)
        if choice == 2:
            data_contact = view.get_data()
            database.get_contact(data_contact)
        if choice == 3:
            data_contact = view.get_data()
            lst_contact = database.select_contact(data_contact)
            print(lst_contact)
            number_contact = view.get_numberContact()
            new_contact = view.enter_data()
            database.change_contact(lst_contact[number_contact-1], new_contact)
        if choice == 4:
            database.get_allContact()
        if choice == 5:
            data_contact = view.get_data()
            lst_contact = database.select_contact(data_contact)
            number_contact = view.get_numberContact()
            database.delete_contact(lst_contact[number_contact-1])
        if choice == 6:
            database.delete_allContact()    
        if choice == 7:
            print("Вы покинули меню...")
            break

menu()