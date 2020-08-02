a = list(input("enter ur word ZOO"))
x = a.count('z')
y = a.count('o')
if x and y > 0:
    if 2 * x == y:
        print("yes")
    else:
        print("no similar word found")
else:
    print('no zoo word found')

