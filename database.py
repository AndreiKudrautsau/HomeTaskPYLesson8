def enter_data(data_contact):
    with open('db.txt', 'a', encoding='utf-8') as file:
        file.writelines(data_contact) 
    print("Телефонная книга обновлена.")

def get_contact(data_contact):
    with open('db.txt', 'r', encoding="utf-8") as file:
        lst_contact = file.readlines()
        count = 0
        print(f"По запросу '{data_contact}' найдены следующие контакты: ") 
        for i in lst_contact:
            if data_contact in i:
                count +=1
                print(f"{count}. {i.strip()}")
        if count == 0:
            print("ничего не найдено - введите новый запрос.")        

def get_allContact():
    with open('db.txt', 'r', encoding="utf-8") as file:
        lst_contact = file.readlines()
        count = 1
        print(f"Список всех контактов: ") 
        for i in lst_contact:
            print(f"{count}. {i.strip()}")
            count += 1
                
def select_contact(data_contact):
    lst_selectContact = []
    with open('db.txt', 'r', encoding="utf-8") as file:
        lst_contact = file.readlines()
        count = 1
        for i in lst_contact:
            if data_contact in i:
                lst_selectContact.append(i)
                print(f"{count}. {i.strip()}")
                count +=1
        return lst_selectContact

def change_contact(old_contact, new_contact):
    lst_allContact = []
    with open('db.txt', 'r', encoding="utf-8") as file:
        lst_allContact = file.readlines()
    with open('db.txt', 'w', encoding="utf-8") as file:    
        for i in lst_allContact:
            if i == old_contact:
                file.write(new_contact)
                continue
            file.write(i)
            print("Запись успешно изменена.")

def delete_contact(data_contact):
    lst_allContact = []
    with open('db.txt', 'r', encoding="utf-8") as file:
        lst_allContact = file.readlines()
    with open('db.txt', 'w', encoding="utf-8") as file:    
        for i in lst_allContact:
            if data_contact == i:
                continue
            file.write(i)
    print("Запись успешно удалена.")

def delete_allContact():
    f = open('db.txt', 'w')    
    f.close()
    print("Все записи успешно удалены.")        
                                   