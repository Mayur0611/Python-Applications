
# accept number from user and print triangle pattern

def main():
    print("Enter number:")
    No=int(input())
    

    for i in range(0,No+1):
        for j in range (0,No-i):
            print("*", end=" ")
        print()


if __name__=="__main__":
    main()
