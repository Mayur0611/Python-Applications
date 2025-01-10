
# python application create two threads evenlist and oddlist
# - evenlist thread gives addition of even numbers from list
# - oddlist thread gives addition of  numbers from list



import threading

def Chk_Even(No):
    Sum = 0
    for i in range(0,len(No)+1):
        if (i % 2 == 0):
            Sum = Sum +  i


    print("Addition of Even Numbers is {} ".format(Sum))

def Chk_Odd(No):
    Sum = 0
    for i in range (0,len(No)+1):
        if (i % 2 != 0):
            Sum = Sum + i

    print("Addition of Odd Numbers is {}".format(Sum))



def main():
    List = [1,2,3,4,5]

    evenlist = threading.Thread(target=Chk_Even,args=(List,))
    oddlist = threading.Thread(target=Chk_Odd, args=(List,))

    evenlist.start()
    oddlist.start()


if __name__=="__main__":
    main()

