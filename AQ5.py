
#Q. program which display 10 to 1 numbers on screen:

def display(No):
    for i in range(No,0,-1):
        print(i,end=" ")

def main():

    print(" Reversely  written numbers from 10 to 1:")
    No = 10
    display(No)


if __name__=='__main__':
    main()