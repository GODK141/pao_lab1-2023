left, year, interest = [int(i) for i in input("Input: borrowed amount, duration(years), annual interest(%) ").split()]
clear = False
must_repay = left * (1+interest/100)
if year > 1:
    for i in range(year-1):
        pay = int(input("Input: pay at the end of year 1 "))
        if pay < must_repay:
            must_repay -= pay
        else:
            clear = True
            break
        must_repay *= (1+interest/100)
if clear:
    print("Output: You already clear your loan")
else:
    print("Output: To clear your loan, you need to repay %.2f at the end of year %d" %(must_repay, year))