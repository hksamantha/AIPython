# Initial balance and purchase amount both you can input as you wish
def account_balance(initial_balance, purchase_amount):
    if purchase_amount==0:
        purchase_amount=0
    elif purchase_amount % 10 >=5:
        purchase_amount=(purchase_amount//10)*10+10 
    else:
        purchase_amount=(purchase_amount//10)*10

    new_balance=initial_balance - purchase_amount
    return new_balance

print(account_balance(int(input("Initial balance: ")), int(input("purchase amount: "))))