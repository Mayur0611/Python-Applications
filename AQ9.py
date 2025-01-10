
#Q. program accept number from the user and return list of even and odd number in range 1 to accepted number from user separately :

def Even_Odd(No):
    even = []
    odd = []

    for i in range(1 ,No+1):
        if i % 2 == 0:
            even.append(i)
        else:
            if i % 2 != 0:
                odd.append(i)

    return print("Even numbers :{} \n Odd numbers :{} ".format(even ,odd))


def main():

    user_input = int(input("Enter the number:"))
    result = Even_Odd(user_input)
    print(result)

if __name__=='__main__':
    main()