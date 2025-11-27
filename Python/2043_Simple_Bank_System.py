class Bank:
    def __init__(self, balance: List[int]):
        self.bank = balance

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if (
            0 <= account1 - 1 <= len(self.bank) - 1
            and 0 <= account2 - 1 <= len(self.bank) - 1
            and self.bank[account1 - 1] >= money
        ):
            self.bank[account1 - 1] -= money
            self.bank[account2 - 1] += money
            return True
        return False

    def deposit(self, account: int, money: int) -> bool:
        if 0 <= account - 1 <= len(self.bank) - 1:
            self.bank[account - 1] += money
            return True
        return False

    def withdraw(self, account: int, money: int) -> bool:
        if 0 <= account - 1 <= len(self.bank) - 1 and self.bank[account - 1] >= money:
            self.bank[account - 1] -= money
            return True
        return False


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)
