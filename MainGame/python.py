class account:
    def account_type(self):
        print(f"general account")


class savingAccount:
    def account_type(self):
        print(f"saving account")


acc1 = account()                
acc2 = savingAccount()
acc1.account_type()
acc2.account_type()