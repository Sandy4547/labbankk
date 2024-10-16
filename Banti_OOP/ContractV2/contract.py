from contract_list import ContractList

class Contract:
    all_contracts = ContractList()
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.all_contracts.append(self)
    def __str__(self):
        return f"Contract:name: {self.name}, email: {self.email}"