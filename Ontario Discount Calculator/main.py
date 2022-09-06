# Ontario Discount Calculator

# Welcome Message
print("Welcome to the Ontario Discount Calculator")

# Command Input
item_price = float(input("What is the price of the item? \n$ "))
discount = int(input("What is the discount percentage? \n% "))

item_discount = discount / 100 * item_price
item_discount = item_price - item_discount
item_discount2 = round(item_discount, 2)
item_discount2 = "{:.2f}".format(item_discount)

discount_save = item_price - item_discount
discount_save2 = round(discount_save, 2)
discount_save2 = "{:.2f}".format(discount_save)

new_total = float(item_discount2) * float(1.13)
new_total2 = round(new_total, 2)
new_total2 = "{:.2f}".format(new_total2)


# Final Results
print(f"---> You save ${discount_save2}!\nYour item with {discount}% discount is: ${item_discount2}.")
print(" ")
print(f"Your new total is ${new_total2} with discounts and taxes included.")