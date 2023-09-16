num = int(input("Input: "))
if num >= 3:
    for i in range(num-1): #top part
        pattern = 0
        for j in range(i+1):
            pattern += 1
            if pattern%2 == 1:
                print("*", end = "")
            else:
                print("0", end = "")
        print(" " * ((num*2)-(2*(i+1))), end = "")
        for j in range(i+1):
            if pattern%2 == 1:
                print("*", end = "")
            else:
                print("0", end = "")
            pattern += 1
        print()
    for j in range(num): #middle part
        if j%2 == 0:
            print("*", end = "")
        else:
            print("0", end = "")
    for j in range(num):
        if j%2 == 0:
            print("*", end = "")
        else:
            print("0", end = "")
    print()
    for i in range(num-1):
        pattern = 0
        for j in range(num-i-1):
            pattern += 1
            if pattern%2 == 1:
                print("*", end = "")
            else:
                print("0", end = "")
        print(" " * ((i+1)*2), end = "")
        for j in range(num-i-1):
            if pattern%2 == 1:
                print("*", end = "")
            else:
                print("0", end = "")
            pattern += 1
        print()
else:
    print("your input is invalid.")