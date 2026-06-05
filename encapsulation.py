class Bankaccount:
    def __init__(self,account_number,balance):
        self.acc_num = account_number
        self.__balance = balance              #private variable created

    
    
    def check_bal(self):
        print(self.__balance)

    def deposit(self,amt):
        self.__balance=self.__balance+amt
        print(self.__balance)

    def withdraw(self,amt):
        if self.__balance>amt:
            self.__balance=self.__balance-amt
            print(self.__balance)
        else:
            print("Insufficient Balance")

yashu = Bankaccount(35,100000)    #creating an object of class Bank account
yashu.check_bal()                 # accessing private variable through methods
yashu.deposit(40000)
yashu.withdraw(20000)
print(yashu.acc_num)
# print(self.__balance)             # private variable cannot be accessed directly and hence name error