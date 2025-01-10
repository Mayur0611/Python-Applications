

# Q. program which contains one function named as ChkNum() which accept one parameter as number,
# if number is even then it display"Even number" otherwise display"odd Number".


def ChkNum(No):
    if No % 2 == 0 :
        print("Even number")
    else:
        if No % 2 != 0:
            print("Odd number")

def main():
     Num = int(input("Please enter the number:"))

     # calling of function
     ChkNum(Num)

if __name__=='__main__':
    main()

