
#Q.  Python application which creats two threads named as even and odd.
#    - even thread display even numbers list and odd thread display odd numbers list:


import threading

def Even_Number(No):
    EvenNumbers = []
    for i in range(1,No+1):
        if (i % 2 == 0):
            EvenNumbers.append(i)
    print("List of Even Numbers:", end=" ")
    print(EvenNumbers)

def Odd_Number(No):
    OddNumbers = []
    for i in range(1,No+1):
        if(i % 2 !=0):
            OddNumbers.append(i)
    print("List of Odd Numbers:",end=" ")
    print(OddNumbers)


def main():
    print("separate out Even and Odd number")

    Numbers = int(input("Enter the number "))

    even = threading.Thread(target=Even_Number,args=(Numbers,))  # even thread

    odd = threading.Thread(target=Odd_Number, args=(Numbers,))   # odd thread

    even.start()
    odd.start()


if __name__=="__main__":
    main()