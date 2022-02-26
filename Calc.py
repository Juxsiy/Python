while True:
    a = input()
    try:
        print(eval(a))
    except Exception:
        print("error")
    c = int(input("введите 1 чтобы продолжить, либо 2 чтобы выйти\n> "))
    if c == 2:
        break
