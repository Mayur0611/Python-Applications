
#Q program accept list and perform filter, map reduce operations on list elements:

from functools import reduce

def Chknum(no):
    if no >= 70 and no<= 90:
        return True

def increase(no):
    return no+10


def product(a,b):
    return a*b


def main():
    print("Enter the number you want to add in list:")
    size=int(input())

    print("Enter numbers:")

    List=[]
    for i in range(0,size,1):
        values=int(input())
        List.append(values)
    print("Data in list is :",List)

    print("Filter operation on list :")
    Chknumber=list(filter(Chknum,List))
    print("Data after filter :",Chknumber)

    print("Map operation on list :")
    Increment=list(map(increase,Chknumber))
    print("Data after Map:",Increment)

    print("Reduce operation on list")
    Multiplication=reduce(product,Increment)
    print(("Data after Reduce:",Multiplication))

if __name__=="__main__":
    main()