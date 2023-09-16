n = int(input("Input: "))
count = 1
for i in range(n):
    print("0\t" * i, end = "")
    for j in range(n-i):
        print(count, end = "\t")
        count += 1
    print()