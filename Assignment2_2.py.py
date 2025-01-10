
#Q Accept number from user and print * pattern

def main():
    print(" How Many time you want to print the pattern:")
    No=int(input())


    for i in range(0,No):
        for j in range (0,No):
            print("*", end=" ")
        print()


if __name__=="__main__":
    main()
