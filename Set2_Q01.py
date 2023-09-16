import math
shape = input("Input a shape T/S/C: ")
d = int(input("Input a length: "))
if shape != "T" or shape != "S" or shape != "C":
    print("Type must be only T/S/C.")
if d >= 0:
    if shape == "T":
        print("The surface area of triangle is %.2f" %((d**2) / 4))
    elif shape == "S":
        print("The surface area of square is %.2f" %((d**2) / 2))
    elif shape == "C":
        print("The surface area of circle is %.2f" %((d**2) * math.pi / 4))
else:
    print("Length must be more than or equal to zero.")