string = input("Input: ")
for i in range(len(string)):
    if string[i].isnumeric():
        for j in range(int(string[i])):
            if string[i] == 0:
                print()
                break
            elif j%3 == 2:
                print("#", end = "")
            else:
                print("*", end = "")
        print()
        