val = input("a, b, c = ").split()
invalid = False
for i in range(3):
    if val[i] != "True" and val[i] != "False":
        invalid = True
if not invalid:
    if val[0] == "False" and val[1] == "False" and val[2] == "True":
        output = "Deny"
    elif val[0] == "False" and val[1] == "True" and val[2] == "False":
        output = "Deny"
    elif val[0] == "False" and val[1] == "True" and val[2] == "True":
        output = "Deny"
    else:
        output = "Grant"
    print(output)
else:
    print("Invalid input")