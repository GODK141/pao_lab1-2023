import math as m
unit = ["cm", "in", "mm"]
d = float(input("Input a circle diameter: "))
d_input = d
d_unit = input("Input a unit of the diameter: ")
a_unit = input("Input a unit of the output area: ")
if d > 0 and a_unit in unit and d_unit in unit:
    if d_unit == "cm": #change d to mm
        d = d * 10
    elif d_unit == "in":
        d = d * 25.4
    area = m.pi * (d**2) / 4 #area in mm
    if a_unit == "cm":
        area = area / (10**2)
    elif a_unit == "in":
        area = area / (25.4**2)
    print("The surface of a circle with a %.2f %s diameter is %.2f square %s." %(d_input, d_unit, area, a_unit))
else:
    print("Invalid input")