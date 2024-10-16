Class ContractList(list)
def search(self, name):
    matching_contract = []
    for c in self:
        if name in c.name:
            matching_contract.append(c)
    return matching_contract
        