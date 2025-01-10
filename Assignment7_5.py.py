

#Q. application accept number from user and return list of its forward and backward pattern in range of user input
#  program contain thread named as Thread1(forForward) and Thread2(forBackward)


import threading

def Forward(No1,No2):
    Forward_pattern=[]

    for i in range (No1,No2+1):
        Forward_pattern.append(i)
    print(Forward_pattern)

def Backward(No1,No2):

    Backward_pattern=[]

    for i in range(No2,No1-1,-1):
        Backward_pattern.append(i)
    print(Backward_pattern)



def main():
    Number1 = int(input("Number range start from:"))
    Number2= int(input("Number range upto:"))


    Thread1 = threading.Thread(target=Forward,args=(Number1,Number2))
    Thread2 = threading.Thread(target=Backward,args=(Number1,Number2))

    Thread1.start()
    Thread2.start()

    Thread1.join()
    Thread1.join()


if __name__=="__main__":
    main()



