

#Q. program which accept number from users and check whether that number is positive or negative or zero:

def checkNum(No):

    if No > 0 :
        print("{} is positive number".format(No))
    elif No < 0 :
        print("{} is negative number".format(No))
    else:
        if No == 0:
            print("it,s Zero")


def main():

    Input= int(input("Enter the number:"))
    checkNum(Input)

if __name__=='__main__':
    main()