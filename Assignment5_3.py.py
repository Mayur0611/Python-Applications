
##Q Application for performing arithmatic operations:

# program contain one class named as Arithmatic
# class contain instance variables as Value1,Value2
# There are instance methods in class as Accept,Addition,Subtraction,Multiplication,Division




class Arithmetic:

    #instance variables:
    def __init__(self):
        self.Value1 = 0
        self.Value2 = 0

    # instance methodas:
    def Accept(self):
        print("Enter first number:")
        self.Value1 = int(input())

        print("Enter second number")
        self.Value2 = int(input())

    def Addition(self):

        Add = self.Value1 + self.Value2
        return print("Addition is {}".format(Add))

    def Subtraction(self):

        Sub = self.Value1 - self.Value2
        return print("Subtraction is {}".format(Sub))

    def Multiplication(self):

        Mult = self.Value1 * self.Value2
        return print("Multiplication is {}".format(Mult))

    def Division(self):

        Div = self.Value1 / self.Value2
        return print(" Division is {}".format(Div))




def main():

     # class object:
    obj = Arithmetic()

    # calling of instance methods
    obj.Accept()
    obj.Addition()
    obj.Subtraction()
    obj.Multiplication()
    obj.Division()



if __name__=="__main__":
    main()