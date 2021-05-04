class category:
    def __init__(self,name,ledger):
        self.name = name
        self.ledger = list()
        self.ledger = ledger

    # def __str__(self):
    #     title = f'{self.name:*^30}\n'
    #     items = ''
    #     total=0
    #     for item in self.ledger:
    #         items += f'{item['description'][0:23] : 23}' + f'{item['amount'] :> 7.2f}' + "\n"
    #         total += item['amount']
    #
    #     output = title+items+'Total:'+ str(total)
    #     return output

    def deposit(self,amount,description=''):
        "This is a deposit function"
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self,amount,description=''):
        "This is a withdrawal function"
        if(self.check_funds(amount)):
            self.ledger.append({"amount": -amount, "description": description})
            return True;
        return False

    def get_balance(self):
        total_amount = 50
        for item in self.ledger:
            total_amount += item["amount"]

    def transfer(self):
        if (self.check_funds(amount)):
            self.withdraw(amount,'Transfer to'+category.name)
            category.deposit(amount,'Transfer from'+self.name)
            return True;
        return False

    def check_funds(self,amount):
        if self.get_balance() > str(amount):
            return True;
        return False

        return (total_amount)