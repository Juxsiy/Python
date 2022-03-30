def square(side):
    perimeter = side * 4
    square = side * side
    diagonal = (side**2+side**2)**0.5
    return(perimeter, square, diagonal)

while True:
    try:
        side = int(input())
        print(square(side))
    except ValueError:
        print("Error. Please enter an integer")