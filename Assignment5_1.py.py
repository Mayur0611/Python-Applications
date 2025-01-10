
##Q Display numbers:

# program contain class name Demo
# Demo class contain two instance variable as No1,No2
# There are two instance methods Fun and Gun which display values in instance variables

class Demo:

    def __init__(self,Value1,Value2):
        self.No1 = Value1
        self.No2 = Value2


    def Fun(self):

        print(self.No1 , self.No2)

    def Gun(self):

        print(self.No1, self.No2)

def main():
    
    obj1=Demo(11,21)
    obj2=Demo(51,101)


    obj1.Fun()
    obj2.Fun()
    obj1.Gun()
    obj2.Gun()

if __name__=="__main__":
    main()