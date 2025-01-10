
# program return the power of two  of given number from user using lambda function :

def main():

    print("Poewr of Two of given number")
    power_Function=lambda A : A**2
    print("Enter the number:")
    No=int(input())
    Power=power_Function(No)
    print("power of given number is",Power)

if __name__=="__main__":
    main()