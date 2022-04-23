def is_year_leap(year):
    if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False


while True:
    try:
        year = int(input())
        print(is_year_leap(year))
    except ValueError:
        print("Error. Please enter an integer")
