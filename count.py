

# program accept number from user and return addition of digits in that number


def Add(no):
    num = no
    sum = 0
    for n in num :
        sum = sum + n
    return sum




def main():

    print("-----Application for addition of digits in numbers----- ")
    Number=int(input("Enter the digit"))


    add = Add(str(Number))
    print("Addition of digits in given number is {}".format(add))


if __name__=='__main__':
    main()