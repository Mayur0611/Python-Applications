
# recursive program which accept number from user and returns summation of digits

def Display_Sum(No):
    Sum=0
    while(No > 0):
        Sum = Sum + (No % 10)
        No=No//10


    print("Sum of digits is :", Sum)


Display_Sum(879)
