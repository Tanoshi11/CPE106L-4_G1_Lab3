"""
File: bank.py
This module defines the Bank class.
"""
import pickle
import random
from savingsaccount import SavingsAccount

class Bank:
    """This class represents a bank as a collection of savings accounts.
    An optional file name is also associated
    with the bank, to allow transfer of accounts to and
    from permanent file storage."""

    def __init__(self, fileName=None):
        """Creates a new dictionary to hold the accounts.
        If a file name is provided, loads the accounts from
        a file of pickled accounts."""
        self.accounts = {}
        self.fileName = fileName
        if fileName is not None:
            try:
                with open(fileName, 'rb') as fileObj:
                    while True:
                        try:
                            account = pickle.load(fileObj)
                            self.add(account)
                        except EOFError:
                            break
            except FileNotFoundError:
                pass

    def __str__(self):
        return '\n'.join(map(str, sorted(self.accounts.values())))

    def makeKey(self, name, pin):
        """Returns a key for the account."""
        return f"{name}/{pin}"

    def add(self, account):
        """Adds the account to the bank."""
        key = self.makeKey(account.getName(), account.getPin())
        self.accounts[key] = account

    def remove(self, name, pin):
        """Removes the account from the bank and
        returns it, or None if the account does
        not exist."""
        key = self.makeKey(name, pin)
        return self.accounts.pop(key, None)

    def get(self, name, pin):
        """Returns the account from the bank,
        or None if the account does not exist."""
        key = self.makeKey(name, pin)
        return self.accounts.get(key)

    def computeInterest(self):
        """Computes and returns the interest on
        all accounts."""
        total = 0
        for account in self.accounts.values():
            total += account.computeInterest()
        return total

    def getKeys(self):
        """Returns a sorted list of keys."""
        return sorted(self.accounts.keys())

    def save(self, fileName=None):
        """Saves pickled accounts to a file. The parameter
        allows the user to change file names."""
        if fileName is not None:
            self.fileName = fileName
        elif self.fileName is None:
            return
        
        with open(self.fileName, 'wb') as fileObj:
            for account in self.accounts.values():
                pickle.dump(account, fileObj)

# Functions for testing
       
def createBank(numAccounts=1):
    """Returns a new bank with the given number of accounts."""
    names = ["Brandon", "Molly", "Elena", "Mark", "Tricia","Ken", "Jill", "Jack"]
    bank = Bank()
    upperPin = numAccounts + 1000
    for pinNumber in range(1000, upperPin):
        name = random.choice(names)
        balance = float(random.randint(100, 1000))
        bank.add(SavingsAccount(name, str(pinNumber), balance))
    return bank


def main():
    bank = createBank(8)

    print(bank)

if __name__ == "__main__":
    main()