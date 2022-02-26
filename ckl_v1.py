from sys import argv

script, user_name, password = argv

work = 1
while True:
    if user_name == "Papug" and password == "1234":
        print(f"Добро пожаловать в программу {script}, {user_name}!")
        selection = input(">\t1)Калькулятор\n>\t2)Конвертер\n>\t")
        if selection == "1":
            choice = int(input("""Что будем делать?\n>\t1)+\n>\t2)-\n>\t3)*\n>\t4)/\n>\t"""))
            a = float(input("Введите первое число\n>\t"))
            b = float(input("Введите второе число\n>\t"))
            if choice == 1:
                c = a + b
                print("Результат: " + str(round(c, 5)))
            elif choice == 2:
                c = a - b
                print("Результат: " + str(round(c, 5)))
            elif choice == 3:
                c = a * b
                print("Результат: " + str(round(c, 5)))
            elif choice == 4:
                c = a / b
                print("Результат: " + str(round(c, 5)))
            else:
                print("Введено неверное значение")
        elif selection == "2":
            choice = input("""\n>\t1)см->м\n>\t2)кг->т\n>\t""")
            if choice == ("1"):
                sm = float(input("Сколько сантиметров?"))
                print(f"Ваш результат {sm / 100} метров")
            elif choice == ("2"):
                kg = float(input("Сколько килограмм?"))
                print(f"Ваш результат {kg / 1000} тонн")
            else:
                print("Введено неверное значение")
        else:
            print("Введено неверное значение")
    else:
        print("Неверный логин или пароль!")
    cont = int(input(">\t1)Продолжить работу\n>\t2)Выход\n>\t"))
    if cont == 2:
        break
