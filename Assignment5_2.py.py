
# program contain one class named as circle
# class contain instance variables as Radius,Area,Circumference
# class contain one class variable name  as PI
# There are instance methods in class as Accept,CalculateArea,CalculateCircumference & Display

class Circle:
    # class variable:
    PI = 3.14

    # create instance variable
    def __init__(self):
        self.Radius = 0.0
        self.Area = 0.0
        self.Circumference = 0.0

    # instance methods:
    def Accept(self):
        print("Enter the value of radius:")
        self.Radius=float(input())

    def CalculateArea(self):


        self.Area = (Circle.PI * self.Radius * self.Radius)


    def CalculateCircumfereence(self):


        self.Circumference = (2 * Circle.PI * self.Radius)


    def Display(self):
        print(" The Area of Circle is :",self.Area)
        print(" The Circumference of circle is :",self.Circumference)


def main():
    #object of class:
    obj = Circle()

    # calling instance methods
    obj.Accept()
    obj.CalculateArea()
    obj.CalculateCircumfereence()
    obj.Display()

if __name__=="__main__":
    main()



