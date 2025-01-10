
# Q.program contain on function named as Add() which accepts two parameter as number and return addition of two numbers:


def Add(No1,No2):
    add = No1 + No2
    return add

def main():
    num1 = float(input("Enter first number:"))
    print()
    num2 = float(input("Enter second number:"))

    Sum = Add(num1,num2)
    print("Addition is {} ".format(Sum))



if __name__=='__main__':
    main()