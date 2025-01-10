
#Q program accepts n numbers from user  add into list and return frequency_count of particular number   in list:


def frequence_count(List,x):
    count = 0
    for element in List:
        if (element == x):
            count = count + 1
    return count

def main():

    print("Enter the number of element you want to add")
    size=int(input())

    print("Enter the numbers in list")
    List=[]
    for i in range(0,size,):
        values = int(input())
        List.append(values)
    print("Data in list:",List)

    print("Find out the frequency of element that you want:")
    x=int(input())

    count = frequence_count(List,x)

    print ("frequency of {} element is {} :".format(x,count))



if __name__=="__main__":
    main()