

#Q program accepts n numbers from user  add into list and return maximum number in list:



def maximum(List):

    max=List[0]
    for i in range(0,len(List),1):
        if max < List[i]:
            max = List[i]
    return max


def main():
    print("Enter the number of element you want to add")
    size=int(input())

    print("Enter the numbers in list")
    List=[]
    for i in range(0,size,):
        values = int(input())
        List.append(values)


    print("Data in list:",List)

    max = maximum(List)
    print("maximum number in the list is",max)


if __name__=="__main__":
    main()