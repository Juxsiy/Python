from random import shuffle

coloda = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

shuffle(coloda)
print(coloda)

count = 0
hands = []

while count < 6:
    b = coloda.pop()
    hands.append(b)
    count += 1

print(hands)
