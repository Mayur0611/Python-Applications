

#Q. application for arithmatic operation using user defined module named as Arithmatic


import Arithmatic
def main ():
    print("Performing the different operation on given parameters")

    print("Enter the first number")
    No1=int(input())

    print("Enter  the second number")
    No2=int(input())

    Addition =Arithmatic.Add(No1,No2)
    print("Addition is:", Addition)

    Subtraction=Arithmatic.Sub(No1,No2)
    print("Subtraction is:", Subtraction)

    Multiplication=Arithmatic.Mult(No1,No2)
    print("Multiplication is:",Multiplication)

    Division=Arithmatic.Div(No1,No2)
    print("Division is:",Division)


if __name__=="__main__":
    main()


