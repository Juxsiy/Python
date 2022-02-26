from sys import argv

script, user_name, password = argv

def Calc(num1, num2, op):
    if op == 1: #сумма
        return num1 + num2
    elif op == 2: #разность
        return num1 - num2
    elif op == 3: #произведение
        return num1 * num2
    elif op == 4: #частное
        return num1 / num2
    else:
        return(print("Ошибка"))
def Konv(num1, op):
    if op == 1: #килограммы в тонны
        return num1 / 1000
    elif op == 2: #сантиметры в метры
        return num1 / 100
    else:
        return(print("Ошибка"))
if user_name == "Papug" and password == "1234":
    print(f"Добро пожаловать в программу {script}, {user_name}!")
    work = 1
    while work == 1:
            choise = int(input("Выберите действие:\n1)Калькулятор\n2)Конвертер\n"))
            num1 = float(input("введите первое число\n"))
            num2 = float(input("введите второе число\n"))
            if choise == 1:
                op = int(input("выберите действие:\n1)сумма\n2)разность\n3)произведение\n4)частное\n"))
                print("Результат:", Calc(num1, num2, op))
            elif choise == 2:
                op = int(input("Выберите действие:\n1)килограммы в тонны\n2)сантиметры в метры\n"))
                print("Результат:", Konv(num1, num2, op))
            else:
                print("Ошибка")
            work = int(input("1)Продолжить работу\n2)Выход\n"))
