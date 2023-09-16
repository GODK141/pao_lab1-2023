import random as rand
char = ["#", "*", "$"]
w = int(input("Rectangle width: "))
h = int(input("Rectangle height: "))
t = int(input("Border thickness: "))
hole_h = int(h - (2*t))
if hole_h > 0:
    for i in range(t):
        for j in range(w):
            print(rand.choice(char), end = "")
        print()
    for i in range(hole_h):
        for j in range(t):
            print(rand.choice(char), end = "")
        print(" " * (w - (2*t)), end = "")
        for j in range(t):
            print(rand.choice(char), end = "")
        print()
    for i in range(t):
        for j in range(w):
            print(rand.choice(char), end = "")
        print()
else:
    for i in range(h):
        for j in range(w):
            print(rand.choice(char), end = "")
        print()