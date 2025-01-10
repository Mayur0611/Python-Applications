
# Q.program which accept one number from user and display space separated  "*" equal to number given by user

def display(No):
    for i in range(No):
        if i <= No:
            print("*",end=" ")

def main():

    print("-------Application for pattern printing---------")
    User = int(input("Enter the value:"))
    display(User)


if __name__=='__main__':
    main()