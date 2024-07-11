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
        self.__iban = iban
        self.__balance = balance
        self.__status = status

    @property  # getter
    def balance(self) -> float:
        return self.__balance

    @property  # getter
    def status(self) -> AccountStatus:
        return self.__status

    @status.setter  # setter
    def status(self, new_status: AccountStatus) -> None:
        if self.__status == AccountStatus.CLOSED:
            raise ValueError("Account is closed.")
        self.__status = new_status

    def withdraw(self, amount: float) -> float:
        # business rule
        if self.__status != AccountStatus.ACTIVE:
            raise ValueError(f"Account {self.__iban} cannot be used since it is not active.")
        # validation
        if amount <= 0:
            raise ValueError("Amount must be positive for withdraw")
        # business rule
        if amount > self.__balance:
            raise ValueError(f"Amount {amount} exceeds balance {self.__balance}")
        self.__balance = self.__balance - amount
        return self.__balance

    def deposit(self, amount: float) -> float:
        # business rule
        if self.__status != AccountStatus.ACTIVE:
            raise ValueError(f"Account {self.__iban} cannot be used since it is not active.")
        # validation
        if amount <= 0:
            raise ValueError("Amount must be positive for deposit")
        self.__balance = self.__balance + amount
        return self.__balance

    def __str__(self) -> str:
        return f"Account [iban: {self.__iban},balance: {self.__balance}, status: {self.__status}]"


# creating a new Account object
acc1: Account = Account("tr1", 100_000, AccountStatus.ACTIVE)  # triggers __init__() method
acc2: Account = Account("tr2", 200_000)
try:
    acc1.deposit(150_000)
    acc1.withdraw(250_000)  # withdraw(acc1, 250_000)
    # error: acc1.balance -= 10_000_000
    print(f"balance: {acc1.balance}")
    print(f"status: {acc1.status}")
    acc1.status = AccountStatus.BLOCKED
    print(f"status: {acc1.status}")
    print(str(acc1))
    print(acc2)
except ValueError as ve:
    print(ve)
