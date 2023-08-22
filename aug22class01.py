menu = {
    "apple": 200,
    "sugar": 100,
    "carrot": 50,
    "rice": 500,
    "water": 80,
    "banana": 250
}
cart = ['banana', 'water', 'apple']

total = 0
for item in cart:
    total += menu[item]
print("cart total is: ", total)
