import budget

food = budget.category('Food','amount')
food.deposit(1000,'Initial deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89,'Restaurant and more food for dessert')
print(food.get_balance())

clothing=budget.category('clothing')
food.transfer(50,clothing)
clothing.withdraw(25.55)
clothing.withdraw(100)
#
entertainment = budget.category('entertainment')
entertainment.deposit(500,'Initial deposit')
entertainment.withdraw(10, 'groceries')
food.transfer(100,entertainment)

print(food)
print(clothing)

