f1 = Friend("Bob", "bob@ksu.ac.th", "123-456-7890")
f2 = Friend("Tom", "tom@ksu.ac.th", "123-456-4321")
f3 = f2

print(f1)
print(f2)
print("ID f1, f2, f3")
print(id(f1))
print(id(f2))
print(id(f3))
print("ID all contracts")
print(id(f1.all_contracts))
print(id(f2.all_contracts))
print(id(f3.all_contracts))

s = Supplier("Pizza Hut", "pizzahut@ksu.ac.th")
s.order("8 Chick Wings")
for p in s.all_contracts:
    print(p)