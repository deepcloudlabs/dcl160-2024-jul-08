"""
Modeling/Abstraction
DDD (Domain-Driven Design)
Domain: Core Banking, Insurance, eCommerce, Telecom, ...
OOP -> Domain Class -> Account, Customer, ...
"""


class Account:
    """
    attributes: iban, balance, status, ... -> data/state/property
    behaviour -> method: constructor ->  __init__
                 business methods: withdraw, deposit, ...
    """

    def __init__(self, iban, balance=100, status="ACTIVE"):
        self.iban = iban
        self.balance = balance
        self.status = status



# creating a new Account object
acc1 = Account("tr1", 100_000)  # triggers __init__() method
acc2 = Account("tr2", 200_000)
