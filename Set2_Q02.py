invalid = False
str1, str2 = input("Please enter your information: ").split(",")
if str1.isnumeric() and str2.isalpha():
    age = int(str1)
    name = str2
    if age > 120 or age < 0:
        invalid = True
elif str2.isnumeric() and str1.isalpha():
    age = int(str2)
    name = str1
    if age > 120 or age < 0:
        invalid = True
else:
    invalid = True
if invalid:
    print("Please enter your complete information.")
else:
    print("Your name is %s." %name)
    print("Your age is %d." %age)
