hour, minute, second = [int(i) for i in input("Input: ").split(":")]
if (hour > 23 or hour < 0) or (minute > 59 or minute < 0) or (second > 59 or minute < 0):
    print("Invalid time")
else:
    time = (hour*60*60) + (minute*60) + second
    print("The number of second =", time)