dna = input("DNA: ")
base = input("base: ")
count = 0
for i in range(len(dna)):
    print("c:", dna[i])
    if dna[i] == base:
        print("True if test")
        count += 1
print("There is %d times that the base %s occur in this DNA" %(count, base))