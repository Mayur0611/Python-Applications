

# Check number is divisible by 5 or not :

def Divisible(No):
    if ( No % 5 == 0 ):
        print("True")
        print("given number is divisible by 5")
    else:
        print("False")
        print("given number is not divisible by 5")

def main():
    print("Enter the Number ")
    Number= int(input())

    Ans=Divisible(Number)



if __name__=="__main__":
    main()