alpha = "abcdefghijklmnopqrstuvwxyz"
char1 = input("Give me a character: ")
char2 = input("Give me another character: ")
if char1 >= char2:
    first = char2
    last = char1
else:
    first = char1
    last = char2
print("Output:")
if first.isalpha() and last.isalpha():
    for i in range(len(alpha)): #find the starting index
        if alpha[i] == first:
            start = i
            break
    for j in range(len(alpha)): 
        print(alpha[start], end = "")
        if alpha[start] == last:
            break
        start += 1
else:
    print("You need to put two characters.")