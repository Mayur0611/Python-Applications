
# Q. program accept name from user and return length of it's name:

def later_length(later):
    count = 0

    for w in later:
        count = count + 1

    return count


def main():

    later = str(input("Enter the name:"))
    count = later_length(later)
    print('length of later is:',count)

if __name__=='__main__':
    main()