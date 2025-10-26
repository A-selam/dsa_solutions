class Bank:

    def __init__(self, balance: List[int]):
        self.balances = [0]
        self.balances.extend(balance)
        self.count = len(self.balances)

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if account1 > self.count or account2 > self.count or self.balances[account1] < money:
            return False
        
        self.balances[account2] += money
        self.balances[account1] -= money
        return True

    def deposit(self, account: int, money: int) -> bool:
        if account > self.count:
            return False
        
        self.balances[account] += money
        return True

    def withdraw(self, account: int, money: int) -> bool:
        if account > self.count or self.balances[account] < money:
            return False
        
        self.balances[account] -= money
        return True
        


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)