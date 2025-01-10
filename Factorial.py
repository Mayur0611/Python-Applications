
# Q. Program accept number from user and return its factorial:


def factorial(No):
    if No ==0:
        return 1
    else:
        fact = 1
        if No > 0:
            for i in range (No,0,-1):
                fact = fact * i


        return fact

def main():
    no = int(input("Enter the number:"))
    fact = factorial(no)
    print("factorial of {} is {} ".format(no,fact))

if __name__=='__main__':
    main()
