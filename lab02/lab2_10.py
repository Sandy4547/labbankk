food_cost = float(input("Enter food cost: "))
trip_cost = float(input("Enter trip: "))

vat_rate = 0.07
food_cost_with_vat = food_cost + (food_cost * vat_rate)

total_cost = food_cost_with_vat + trip_cost

print("Food cost with VAT (7%) is", int(food_cost_with_vat), "baht.")
print("Total cost is", int(total_cost), "baht.")

# Enter money and calculate change
money_paid = float(input("Enter money to pay: "))
change = money_paid - total_cost

print("Change are:")

# List of denominations in baht
denominations = [500, 100, 50, 20, 10, 5, 1]

# Loop through each denomination and calculate the number of each
for denom in denominations:
    num_denom = int(change // denom)
    change -= num_denom * denom
    print(f"{denom} baht: {num_denom}.0")

# Output the total change
print("Total is", round(money_paid - total_cost, 1), "baht.")
