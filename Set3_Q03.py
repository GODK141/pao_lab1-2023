import math as m
unit = ["ft", "in"]
volume = float(input("Input a sphere volume: "))
first_volume = volume
v_unit = input("Input the unit of the volume: ")
r_unit = input("Input the unit of the sphere radius length: ")
if volume > 0 and v_unit in unit and r_unit in unit:
    if v_unit == "ft":
        volume *= 12**3 #in cubic inch
    radius = (3*volume/4/m.pi)**(1/3)
    if r_unit == "ft":
        radius /= 12
    print("The radius of a sphere with a volume of %.2f cubic %s is %.2f %s." %(first_volume, v_unit, radius, r_unit))
else:
    print("Invalid input")
    