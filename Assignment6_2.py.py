

#Q. Program accepts name and amount value from user and perform different operations using this information

# program contain  one class named as BankAccount:
# BankAccount class contain class variable named as ROI(rate of interest)
# class contain instance variable named as Name & Amount
# class contain instance method named as Display,Deposit,Withdraw,CalculateInterest


class BankAccount:

    ROI = 10.5

    def __init__(self):
        self.Name = " "
        self.Amount = 0


    def Display(self):
        print("Entet the name of account holder:")
        self.Name = input()

        print("Enter the Amount:")
        self.Amount = int(input())

    def Deposit(self):
        print("How many amount you want to Deposit:")
        Deposited_ammount = int(input())
        Deposit= self.Amount + Deposited_ammount

        print("The Amount after deposit is {}".format(Deposit))

    def Withdraw(self):
        print("How many amount you want to Withdraw:")
        Withdraw_ammount = int(input())
        Withdraw = self.Amount - Withdraw_ammount

        print("The Amount after Withdraw is {}".format(Withdraw))

    def CalculateIntrest(self):

        print("Interast on Your Account Balance:")
        print(" Enter No of years: ")
        Year = int(input())

        Intrest = ( self.Amount * BankAccount.ROI * Year)/100

        print("The intrest on {} for {} years is,{}".format(self.Amount,Year,Intrest))

        Total_Account_Balance = self.Amount + Intrest
        print("Account Balance Afer getting interest is {}".format(Total_Account_Balance))


def main():
    Obj= BankAccount()

    Obj.Display()
    print("----------------------------------")

    Obj.Deposit()
    print("----------------------------------")


    Obj.Withdraw()
    print("----------------------------------")


    Obj.CalculateIntrest()
    print("----------------------------------")




if __name__=="__main__":
    main()








