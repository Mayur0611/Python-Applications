

#Q program accept list and perform filter, map reduce operations on list elements:
# filter = even numbers list
# map = square of filterd list
# reduce = Addition of map list

from functools import reduce

def ChkEven(no):
    if no % 2 == 0:
        return True

def square(no):
    return no**2


def Addition(a,b):
    return a+b


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
    Filter=list(filter(ChkEven,List))
    print("Data after filter :",Filter)

    print("Map operation on list :")
    Map=list(map(square,Filter))
    print("Data after Map:",Map)

    print("Reduce operation on list")
    Reduce=reduce(Addition,Map)
    print(("Data after Reduce:",Reduce))

if __name__=="__main__":
    main()