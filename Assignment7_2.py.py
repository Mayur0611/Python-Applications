
#Q. application creates two thread named as evenfactors & oddfactors
#   -both threads accept one parameter as integer
#   -evenfactors thread display sum of evenfactors and oddfactors thread dispay sum of odd factors


import threading

def Evenfactore(No):
    Sum=0
    for i in range(1,No+1):
        if (No % i == 0):
            if (i % 2 ==0):
                Sum = Sum + i


    print("Addition of Even factors is {}".format(Sum),'\n')

def Oddfactor(No):
    Sum = 0
    for i in range (1,No+1):
        if (No % i == 0):
            if (i % 2 != 0):
                Sum = Sum + i

    print("Addition of Odd factors is {}".format(Sum),'\n')


def main():
    print(" ---------------------Application for addition of factors-------------------")

    print("Enter the number:")
    Number=int(input())

    evenfactor = threading.Thread(target= Evenfactore,args=(Number,))
    oddfactor = threading.Thread (target= Oddfactor,args=(Number,))

    evenfactor.start()
    oddfactor.start()



    print("Exit from main...........")


if __name__=="__main__":
    main()



