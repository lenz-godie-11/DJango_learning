"""Banking system"""




# the introduction to our banking system 


class Bank:

    def __init__(self,  bankName ):

         self.CustmerAccounts = {}
         self.bankName = bankName
    
    def add_account(self, name, accountNumber, status, pin):
        account = CustomerAccount(name, accountNumber, status, pin)

        self.customerAccounts[accountNumber] = account

        
# a class for the user account 

class CustomerAccount:

    def __init__(self, name , accountNumber , status ,pin , balance = 0):

        self.name = name
        self.accountNumber = accountNumber
        self.status = status 
        self.__pin = pin
        self._balance = balance


    def set_account_details(self, pin , balance = 0):

        self.__pin = pin
        self._balance = balance


    def deposit(self , balance):

        self._balance += balance


    def withdraw(self , amount ):

              if amount <= self._balance:
                   self._balance -=amount
                   return True
              else:
                    return False
             






