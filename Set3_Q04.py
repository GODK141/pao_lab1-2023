width, height = [int(i) for i in input("Input: ").split()]
if 1 <= width <=9 and 1 <= height <= 9:
    start_forward = 1
    start_backward = width
    for i in range(height):
        forward = start_forward
        backward = start_backward
        for j in range(width):
            if i%2 == 0:
                if (forward) > width:
                    forward = 1
                print(forward, end = "")
                forward += 1
            else:
                if (backward) < 1:
                    backward = width
                print(backward, end = "")
                backward -= 1
        if i%2 == 0:
            start_forward += 1
        else:
            start_backward -= 1
        print()
else:
    print("Invalid input")