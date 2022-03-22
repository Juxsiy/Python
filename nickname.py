from itertools import *
nick = input()
if nick.isalpha():
    words = []
    for i in nick:
        words.append(i)
    new_words = []
    for item in words: 
        if item not in new_words:
            new_words.append(item)
    sort = []
    for i in permutations(new_words):
        sort.append((" ".join(i)).replace(' ', ''))
    sort.sort()
    for i in sort:
        print(i)
else: print("Impossible")
