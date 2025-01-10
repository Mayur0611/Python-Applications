

#Q program accepts n numbers from user  add into list and return addition of numbers in list


def Addition(List):
    sum=0
    for i in List:
        sum=sum+i
    return sum


def main():

    print("How many number of elements you want to enter into list : ")
    iSize = int(input())

    List = []
    print("Please enter the numbers ")
    for iCnt in range(0, iSize, 1):
        Value = eval(input())
        List.append(Value)

    print("Data in list : ", List)

    add = Addition(List)

    print("Addition of numbers in list is {}".format(add))


if __name__ == "__main__":
    main()