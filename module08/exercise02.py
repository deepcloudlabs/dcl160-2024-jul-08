"""
Modeling/Abstraction
DDD (Domain-Driven Design)
Domain: Core Banking, Insurance, eCommerce, Telecom, ...
OOP -> Domain Class -> Account, Customer, ...
"""
from enum import Enum


# inheritance
class AccountStatus(Enum):
    ACTIVE = 100
    BLOCKED = 200
    CLOSED = 300


class Account:
    """
    attributes: iban, balance, status, ... -> data/state/property
    behaviour -> method: constructor ->  __init__
                 business methods: withdraw, deposit, ...
    """

    def __init__(self, iban: str, balance: float = 100, status: AccountStatus = AccountStatus.ACTIVE) -> None:
        self.iban = iban
        self.balance = balance
        self.status = status

    def withdraw(self, amount: float) -> float:
        # business rule
        if self.status != AccountStatus.ACTIVE:
            raise ValueError(f"Account {self.iban} cannot be used since it is not active.")
        # validation
        if amount <= 0:
            raise ValueError("Amount must be positive for withdraw")
        # business rule
        if amount > self.balance:
            raise ValueError(f"Amount {amount} exceeds balance {self.balance}")
        self.balance = self.balance - amount
        return self.balance

    def deposit(self, amount: float) -> float:
        # business rule
        if self.status != AccountStatus.ACTIVE:
            raise ValueError(f"Account {self.iban} cannot be used since it is not active.")
        # validation
        if amount <= 0:
            raise ValueError("Amount must be positive for deposit")
        self.balance = self.balance + amount
        return self.balance

    def __str__(self) -> str:
        return f"Account [iban: {self.iban},balance: {self.balance}, status: {self.status}]"


# creating a new Account object
acc1: Account = Account("tr1", 100_000, AccountStatus.BLOCKED)  # triggers __init__() method
acc2: Account = Account("tr2", 200_000)
try:
    acc1.deposit(150_000)
    acc1.withdraw(250_000)  # withdraw(acc1, 250_000)
    print(f"balance: {acc1.balance}")
    print(str(acc1))
    print(acc2)
except ValueError as ve:
    print(ve)
