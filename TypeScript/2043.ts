class Bank {
    private bank: number[];
    constructor(balance: number[]) {
        this.bank = balance;
    }

    transfer(account1: number, account2: number, money: number): boolean {
        if (0 <= account1 - 1 && account1 - 1 < this.bank.length 
            && 0 <= account2 - 1 && account2 - 1 < this.bank.length 
            && this.bank[account1 - 1] >= money) {
            this.bank[account1 - 1] -= money;
            this.bank[account2 - 1] += money;
            return true;
        }
        return false;
    }

    deposit(account: number, money: number): boolean {
        if (0 <= account - 1 && account - 1 < this.bank.length) {
            this.bank[account - 1] += money;
            return true;
        }
        return false;
    }

    withdraw(account: number, money: number): boolean {
        if (0 <= account - 1 && account - 1 < this.bank.length 
            && this.bank[account - 1] >= money) {
            this.bank[account - 1] -= money;
            return true;
        }
        return false;
    }
}
