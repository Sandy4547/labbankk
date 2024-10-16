from contract import Contract

c1 = Contract("Tom", "tom@ksu.ac.th")
c2 = Contract("Bob", "bob@ksu.ac.th")
c3 = Contract("Sai", "Sai@ksu.ac.th")
c4 = Contract("Tomy", "tomy@ksu.ac.th")

print("All contracts")
for c in Contract.all_contracts:
    print(c)

print()
print("All contracts with name Tom")
for c in Contract.all_contracts.search("Sai"):
    print(c)