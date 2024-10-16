food_cost = float(input("Enter food cost: "))
trip_cost = float(input("Enter trip: "))

vat_rate = 0.07
food_cost_with_vat = food_cost + (food_cost * vat_rate)

total_cost = food_cost_with_vat + trip_cost

print("Food cost with VAT (7%) is", int(food_cost_with_vat), "baht.")
print("Total cost is", int(total_cost), "baht.")