
#Q. program accept number from user and returns it's factorial:

def fact(x):
    if( x == 0) :
        return 1
    else:
        return ( x * fact(x-1))

def main ():
    print("Enter the number:")
    No=int(input())
    Factorial=fact(No)
    print("factorial is:",Factorial)





if __name__=="__main__":
    main()


