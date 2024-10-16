food_cost = float(input("Enter food cost: "))
trip_cost = float(input("Enter trip: "))

vat_rate = 0.07
food_cost_with_vat = food_cost + (food_cost * vat_rate)

# Round the total cost to avoid floating-point issues
total_cost = round(food_cost_with_vat + trip_cost)

print("Food cost with VAT (7%) is", int(round(food_cost_with_vat, 0)), "baht.")
print("Total cost is", int(total_cost), "baht.")

# Enter money and calculate change
money_paid = float(input("Enter money to pay: "))
change = money_paid - total_cost

# Ensure the change is rounded to the nearest 0.1 baht and correctly displays 378.0 baht
change = round(change, 1)

print("Change is", change, "baht.")