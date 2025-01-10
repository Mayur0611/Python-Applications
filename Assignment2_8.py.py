
#Q program accept one number from user and return number pattern
def main():
    print("Enter the input")
    No=int(input())

    for i in range (1,No+1):
        for j in range(1, i+1 ):
            print(j,end=" ")
        print()




if __name__=="__main__":
    main()