
#Q. program accept number from user and check it is prime,perfect,calculate it's factors and give it's addition

# program contain one class named as Numbers
# instance variable name as Value
# instance methods named as CheckPrime,CheckPerfect,Factors,SumFactors

class Numbers:

    def __init__(self,No):
        self.Value = No     # instance variable


    def Chkprime(self):
        if self.Value > 1:
            for i in range (2,self.Value) :
                if (self.Value % i == 0):
                    print(self.Value,"is not prime number")
                    break
            else:
                print(self.Value ,"is a prime number")


    def chkperfect(self):
        Sum = 0
        for i in range (1,self.Value):
            if (self.Value % i == 0):
                Sum = Sum +i
        if (Sum == self.Value):
            print(self.Value, "is perfect number")
        else:
            print(self.Value, "is not perfect number")

    def Factors(self):
        print("Factors of {} are :".format(self.Value),end="")

        for i in range(1,self.Value+1):
            if(self.Value % i == 0):
                print(i,end=" , ")


    def SumFactors(self):

        Sum = 0
        for i in range(1,self.Value+1):
            if(self.Value % i == 0):
                Sum = Sum + i
        print("Sum of factors is:",Sum)


def main():
    print("Enter the number:")
    No=int(input())
    obj=Numbers(No)

    obj.Chkprime()
    obj.chkperfect()
    obj.Factors()
    obj.SumFactors()

if __name__=="__main__":
    main()