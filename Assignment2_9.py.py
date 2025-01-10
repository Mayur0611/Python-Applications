

#Q Program accepts number from user and return return count of digits in that number

def main():
    No=int(input())
    Digit_count=0
    while (No>0):
        Digit_count=Digit_count+1
        No=No//10
    print("COUNT:",Digit_count)


if __name__=="__main__":
    main()

