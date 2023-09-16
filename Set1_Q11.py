side = []
side.append(int(input("Input: a=? ")))
side.append(int(input("Input: b=? ")))
side.append(int(input("Input: c=? ")))
side.sort()
if side[2] < (side[0] + side[1]):
    print("Output: Form a triangle")
else:
    print("Output: Can't form a triangle")