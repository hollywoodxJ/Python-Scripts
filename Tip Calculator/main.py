# Tip Calculator App

# Welcome Message
print("Welcome to the tip calculator!")


# Command Input
bill = float(input("What was the total bill? \n$ "))
percentage = int(input("What percentage tip would you like to give? 10, 12 or 15? or other? \n% "))
split = int(input("How many people to split the bill? \n" ))


# Calculations
total_tip = percentage / 100 * bill
total_tip2 = round(total_tip, 2)
total_tip2 = "{:.2f}".format(total_tip)

final_each_tip = total_tip / split
final_each_tip2 = round(final_each_tip, 2)
final_each_tip2 = "{:.2f}".format(final_each_tip)

final_amount = (percentage / 100 * bill + bill) / split
final_amount2 = round(final_amount, 2)
final_amount2 = "{:.2f}".format(final_amount)

no_tip = bill / split
final_no_tip2 = round(no_tip, 2)
final_no_tip2 = "{:.2f}".format(no_tip)

new_total = bill + total_tip
final_new_total2 = round(new_total, 2)
final_new_total2 = "{:.2f}".format(new_total)


# Final Results
print(f"---> The Total tip is ${total_tip2}.")
print(f"Each person should pay: ${final_each_tip2} in tips.")
print(f"Each person should pay: ${final_amount2} with tip included.")
print(f"Each person should pay: ${final_no_tip2} without tip included.")
print(f"---> The new total with {percentage}% tip is ${final_new_total2}.")