food_amount = float(input("please enter the food amount: "))
tip_percentage = float(input("please enter the percentage you would like to tip: ")) / 100
total = food_amount * tip_percentage
amount = (total + food_amount)
print(f"tip amount: ${total}")
print('$' + str(amount))

# food amount
