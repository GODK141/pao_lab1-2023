valid = False
spchar = ["#", "$", "@", "*", "^"]
char = input("Enter a special character: ")
size = int(input("Enter the size of the pattern: "))
option = int(input("Enter option for the pattern: "))
if char in spchar:
    if size > 0:
        if option == 1 or option == 2:
            valid = True
if not valid:
    print("Wrong input values.")
else:
    if option == 1:
        for i in range(size):
            print("." * i, end = "")
            print(char, end = "")
            print("." * (size-i-1))
    elif option == 2:
        for i in range(size):
            print("." * (size-i-1), end = "")
            print(char, end = "")
            print("." * i)