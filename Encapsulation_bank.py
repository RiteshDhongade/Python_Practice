class bank_account:
    def __init__(self , balance ) :
        self.__balance = balance
    def deposit(self , amount ) :
        self.__balance = self.__balance + amount
    def withdraw(self , amount) :
        if self.__balance >= amount :
            self.__balance = self.__balance - amount
            return True
        else :
            return False
    def get_balance(self) :
        return self.__balance