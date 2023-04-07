import os


def add_contact(file) -> str:
    contact = {"Фамилия": None, "Имя": None, "Отчество": None, "Номер телефона": None}
    for key in contact.keys():
        contact[key] = input(f"Введите {key}: ")
    with open(file, "a", encoding="UTF-8") as f:
            print(*list(contact.values()), file=f)
    print("Контакт добавлен!")


def find_contact(file):
    with open(file, "r", encoding="UTF-8") as f:
        contact = {"Фамилия": None, "Имя": None, "Отчество": None, "Номер телефона": None}
        for key in contact.keys():
            contact[key] = input(f'Введите {key} или "Enter": ')
        for line in f:
            name = line.split()
            if contact["Фамилия"].casefold() not in name[0].casefold() or contact["Имя"].casefold() not in name[
                1].casefold() or contact["Отчество"].casefold() not in name[2].casefold() or contact[
                "Номер телефона"].casefold() not in name[3].casefold():
                continue
            print(" ".join(name))
            if input("Вы искали этот контакт? (+/-): ") == "+":
                return line
        print("Контакт не найден")
        return find_contact(file)


def delite_contact(file):
    print("Выберите контакт: ")
    name = find_contact(file)
    print(name)
    with open("tempo_boost.txt", "w", encoding="UTF-8") as dest, open(file, "r", encoding="UTF-8") as origin:
        for line in origin:
            if name != line and line.strip() != "":
                print(line.strip(), file=dest)
    print("Контакт удален!")
    os.remove("contacts.txt")
    os.rename("tempo_boost.txt", "contacts.txt")


def change_contact(file):
    print("Выберите контакт: ")
    name = find_contact(file)
    print(name)
    with open("tempo_boost.txt", "w", encoding="UTF-8") as dest, open(file, "r", encoding="UTF-8") as origin:
        for line in origin:
            if name != line:
                print(line.strip(), file=dest)
            else:
                contact = {"Фамилия": 0, "Имя": 1, "Отчество": 2, "Номер телефона": 3}
                for key, val in contact.items():
                    if input(f"{key} {name.split()[val]} изменить? (+/-): ") == "+":
                        contact[key] = input(f"{key}: ")
                    else:
                        print(name.split())
                        contact[key] = name.split()[val]
                print(*list(contact.values()), file=dest)
    print("Контакт изменён!")
    os.remove("contacts.txt")
    os.rename("tempo_boost.txt", "contacts.txt")


def choose_action():
    print("Здравствуйте!\nЧтобы воспользоваться телефонным справочником введите:\n1: чтобы найти контакт\n2: чтобы "
          "добавить контакт\n3: чтобы изменить контакт\n4: чтобы удалить контакт\n5: закончить работу\n")
    act = input("Выберите действие: ")
    if act not in "1234":
        act = "5"
    return act