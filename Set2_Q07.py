import math as m
a, b, c = input("Please enter an input: ").split("*")
choice = input("Please enter your choice (1 or 2): ")
valid = False
if a.isnumeric() and b.isnumeric() and c.isnumeric() and (choice == "1" or choice == "2"):
    ab = a+b
    a, b, c, ab = int(a), int(b), int(c), int(ab)
    if a > 0 and b > 0 and c > 0:
        valid = True
if valid:
    if choice == "1":
        output = a + m.sqrt((b**2) + (c**3))
    else:
        output = ab%c
    print("The output is %.2f" %output)
else:
    print("Invalid inputs")