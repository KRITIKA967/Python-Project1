print("Hello Sir/Ma'am")
print("Welcome to our Restaurant ")
print("This is our menu")
Menu = {
    "Pizza" : 40,
    "Pasta" : 50,
    "Burger" : 60,
    "Salad" : 70,
    "Coffee" : 80,
}
print("Pizza : Rs40 \n Pasta : Rs50 \n Burger : Rs60 \n Salad : Rs70 \n Coffee : Rs80 ")
total_amount = 0
Order = input("Enter your order :")
if Order in Menu:
    total_amount += Menu[Order]
    print("Your order is placed successfully")
else:
    print("This item not exist in the Menu till yet.")
anything_else = input("Please enter answer if you want anything else in Yes/No")
if anything_else == "Yes":
    final_order = input("Please enter your item :")
if final_order in Menu:
    total_amount += Menu[final_order]
    print("Your order is added successfully.")
else:
    print("This item not exist in Menu till yet.")
print(f"Total amount of items is {total_amount}")
print("Thanks for providing us this oppertunity to serve you.")