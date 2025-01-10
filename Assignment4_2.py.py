
# Multiplication of two numbers using lambda function:\

def main():
    print("Multiplication of two numbers")

    Multiplication = lambda A,B:(A*B)

    print("Enter first number:")
    value1=int(input())

    print("Enter second numbeer:")
    value2=int(input())

    Ans=Multiplication(value1,value2)
    print("Multiplication of given numbers is :",Ans)

if __name__=="__main__":
    main()


