def add_contact(file):
    contact = {"Фамилия": None, "Имя": None, "Отчество": None, "Номер телефона": None}
    for key in contact.keys():
        contact[key] = input(f"Введите {key}: ")
    with open(file, "a", encoding="UTF-8") as f:
            print(*list(contact.values()), file=f)


def find_contact(file):
    with open(file, "r", encoding="UTF-8") as f:
        contact = {"Фамилия": None, "Имя": None, "Отчество": None, "Номер телефона": None}
        for key in contact.keys():
            contact[key] = input(f'Введите {key} или "Enter": ')
        for line in f:
            name = line.split()
            if (contact["Фамилия"].casefold() in name[0].casefold()) and (contact["Имя"].casefold() in name[1].casefold()) and\
                    (contact["Отчество"].casefold() in name[2].casefold()) and (contact["Номер телефона"].casefold() in name[3].casefold()):
                        print(" ".join(name))
                        if input("Вы искали этот контакт? (+/-): ") == "+":
                            return line
        print("Контакт не найден")
        return find_contact(file)


