import math
min, max = input("Please enter two integers: ").split()
if min.isnumeric() and max.isnumeric():
    min, max = int(min), int(max)
    if min > max:          #swap
        temp = min
        min = max
        max = temp
    sum = 0
    for i in range(max-min+1):
        sum += (min+i)
    print("The minimum number is %d" %min)
    print("The maximum number is %d" %max)
    print("The square root of the summation is %.2f" %(math.sqrt(sum)))
else:
    print("Invalid inputs")
