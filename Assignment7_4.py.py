
#Q.  Application accept string from user and return count of upper,lower and numeric case separately
# program contain threads named as  capital , small and digit and threads scheduled one by one


import threading

def uppere_case(String):
    count1 = 0

    for char in String:
        if (char.isupper() == True):
            count1 = count1 + 1

    return print("upper case :",count1,'\n')


def lower_case(String):
    count2 = 0

    for char in String:
        if (char.islower() == True):
            count2 = count2 + 1

    return print('lower case:',count2,'\n')


def numeric_case(String):
    count3 = 0

    for char in String:
        if (char.isnumeric() == True):
            count3 = count3 + 1

    return print("numeric case:",count3,'\n')



def main():

    String = input("Please enter the string:")


    capital = threading.Thread(target=uppere_case,args=(String,))
    small = threading.Thread(target=lower_case,args=(String,))
    digit = threading.Thread(target=numeric_case,args=(String,))




    capital.start()
    small.start()
    digit.start()


    capital.join()
    small.join()
    digit.join()




if __name__=="__main__":
    main()



