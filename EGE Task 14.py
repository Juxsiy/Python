x= 49**6+7**18-21
s=''

while x>0:
    s = s + str(x%7)
    x = x // 7

print(s.count('6'))