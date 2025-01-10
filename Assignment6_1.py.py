

# program in which instance variable accept value name and auther from user and increment value of NoOfBooks by one

class BookStore:

    NoOfBooks = 0     # class variable

    def __init__(self):    # instance variable
        self.Name = " "
        self.Author = ""


    def Display(self):     # instance method

        print("Enter name of book:")
        self.Name = input()

        print("Enter name of author")
        self.Author = input()


        print("Number of books:")
        No_of_Books = BookStore.NoOfBooks + (int(input()) + 1)

        print("{} by {} . No of Books {}".format(self.Name,self.Author,No_of_Books))

def main():
    Obj1 = BookStore()
    Obj1.Display()

    Obj2 = BookStore()
    Obj2.Display()

if __name__=="__main__":
    main()