"""Task 02 — Bank Account, including a rollback-safe transfer."""


def check_amount(amount):
    if (isinstance(amount, bool)
            or not isinstance(amount, (int, float))
            or amount <= 0
            or amount == float("inf")
            or amount != amount):
        raise ValueError("Amount must be a positive finite number")


class BankAccount:
    bank_name = "National Bank"

    def __init__(self, owner, balance, account_number):
        if not isinstance(balance, (int, float)) or isinstance(balance, bool):
            raise ValueError("Initial balance must be numeric")
        if not 0 <= balance < float("inf"):
            raise ValueError("Initial balance must be finite and non-negative")
        self.owner = owner
        self.balance = balance
        self.account_number = account_number

    def deposit(self, amount):
        check_amount(amount)
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        check_amount(amount)
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount
        return self.balance

    def get_balance(self):
        return self.balance

    def transfer(self, amount, target_account):
        check_amount(amount)
        if not isinstance(target_account, BankAccount):
            raise TypeError("Target must be a BankAccount")
        if target_account is self:
            raise ValueError("Cannot transfer to the same account")
        if amount > self.balance:
            raise ValueError("Insufficient funds")

        previous_source = self.balance
        previous_target = target_account.balance
        try:
            self.withdraw(amount)
            target_account.deposit(amount)
        except Exception:
            self.balance = previous_source
            target_account.balance = previous_target
            raise


def demo():
    accounts = [
        BankAccount("Ali", 1000, "001"),
        BankAccount("Vali", 500, "002"),
        BankAccount("Sardor", 200, "003"),
    ]
    accounts[0].deposit(500)
    accounts[0].withdraw(200)
    accounts[0].transfer(300, accounts[1])
    for account in accounts:
        print(account.owner, account.get_balance())


if __name__ == "__main__":
    demo()
