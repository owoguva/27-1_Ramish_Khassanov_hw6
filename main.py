import re

while True:
    print("Меню:")
    print("1 - Считать имена и фамилии")
    print("2 - Считать все емайлы")
    print("3 - Считать названия файлов")
    print("4 - Считать цвета")
    print("5 - Выход")

    choice = input("Выберите опцию: ")
    if choice == "1":
        # 1 Считываем все имена и фамилии
        with open("MOCK_DATA.txt", "r") as f:
            data = f.read()
        names = re.findall(r"[A-Z][a-z]*\s[A-Z][a-z]*[A '-Z']*[a-z]*", data)

        # Сохраняем имена и фамилии в файл names.txt
        with open("names.txt", "w") as f:
            for name in names:
                f.write(name + "\n")
        print("Имена и фамилии сохранены в файл names.txt")
    elif choice == "2":
        # 2Считываем все емайлы
        with open("MOCK_DATA.txt", "r") as f:
            data = f.read()
        emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', data)
        # Сохраняем емайлы в файл emails.txt
        with open("emails.txt", "w") as f:
            for email in emails:
                f.write(email + "\n")
        print("Емайлы сохранены в файл emails.txt")
    elif choice == "3":
        # 3Считываем названия файлов
        with open("MOCK_DATA.txt", "r") as f:
            data = f.read()
        file_names = re.findall(r'\b\w+\.\w{2,3}\b', data)
        # Сохраняем названия файлов в файл filenames.txt
        with open("file_names.txt", "w") as f:
            for filename in file_names:
                f.write(filename + "\n")
        print("Названия файлов сохранены в файл filenames.txt")
    elif choice == "4":
        # 4Считываем цвета
        with open("MOCK_DATA.txt", "r") as f:
            data = f.read()
        colors = re.findall(r'#[0-9A-Fa-f]{6}\b', data)
        # Сохраняем цвета в файл colors.txt
        with open("colors.txt", "w") as f:
            for color in colors:
                f.write(color + "\n")
        print("Цвета сохранены в файл colors.txt")
    elif choice == "5":
        # 5Выходим из программы
        break
    else:
        print("Работа завершена")

