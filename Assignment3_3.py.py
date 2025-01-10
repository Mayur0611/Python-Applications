

#Q program accepts n numbers from user  add into list and return minimum number in list:


def minimum (List):

    min = List[0]
    for i in range(0, len(List), 1):
        if min > List[i]:
            min = List[i]
    return min


def main():

    print("Enter the number of element you want to add into list:")
    size=int(input())

    print("Enter the numbers in list")
    List=[]
    for i in range(0,size,):
        values = eval(input())
        List.append(values)


    print("Data in list:",List)

    min =minimum(List)
    print("minimum number in the list is",min)


if __name__=="__main__":
    main()