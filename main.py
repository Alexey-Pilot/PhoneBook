import functions as f
file_root = r'C:\Users\alexr\PycharmProjects\PhoneBook\contacts.txt'

while (action := f.choose_action())  != "5":
    if action == "1":
        f.find_contact(file_root)
    elif action == "2":
        f.add_contact(file_root)
    elif action == "3":
        f.change_contact(file_root)
    else:
        f.delite_contact(file_root)
print("Спасибо, что воспользовались нашим справочником!")
