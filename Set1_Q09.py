speed = int(input("Enter speed in mph: "))
dist = int(input("Enter distance in miles: "))
option = input("Enter output format (D or M): ")
d = dist/speed
hr = dist//speed
min = (dist%speed)/speed*60
if option == "D":
    print("At %d mph, it will take\n%.2f hours to travel %d miles." %(speed, d, dist))
elif option == "M":
    print("At %d mph, it will take\n%d hours and %d minutes to travel %d miles." %(speed, hr, min, dist))
else:
    print("Invalid input")
