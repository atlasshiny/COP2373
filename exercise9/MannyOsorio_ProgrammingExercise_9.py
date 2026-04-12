def main():
    class BankAcct:
        """Simple bank account class.

        Attributes:
            name (str): account holder's name
            account_number (str): account identifier
            balance (float): current balance
            interest_rate (float): annual interest rate as a decimal (e.g. 0.05 for 5%)
        """

        def __init__(self, name, account_number, amount=0.0, interest_rate=0.0):
            self.name = str(name)
            self.account_number = str(account_number)
            self.balance = float(amount)
            self.interest_rate = float(interest_rate)

        def set_interest_rate(self, rate):
            """Set the annual interest rate (decimal)."""
            self.interest_rate = float(rate)

        def deposit(self, amount):
            """Deposit a positive amount into the account and return new balance."""
            amount = float(amount)
            if amount <= 0:
                raise ValueError("deposit amount must be positive")
            self.balance += amount
            return self.balance

        def withdraw(self, amount):
            """Withdraw a positive amount if funds available and return new balance."""
            amount = float(amount)
            if amount <= 0:
                raise ValueError("withdrawal amount must be positive")
            if amount > self.balance:
                raise ValueError("insufficient funds")
            self.balance -= amount
            return self.balance

        def get_balance(self):
            """Return the current balance."""
            return self.balance

        def calc_interest(self, days):
            """Calculate interest for given number of days on the current balance.

            Uses simple interest: interest = balance * rate * (days / 365)
            Does not modify the balance.
            """
            days = float(days)
            if days < 0:
                raise ValueError("days must be non-negative")
            return self.balance * self.interest_rate * (days / 365.0)

        def __str__(self):
            return (
                f"Account({self.account_number}) {self.name}: "
                f"Balance=${self.balance:,.2f}, Rate={self.interest_rate * 100:.2f}%"
            )


    def test_bankacct():
        """Run simple tests demonstrating BankAcct functionality."""
        account = BankAcct("Bob Lewis", "25321", amount=1000.0, interest_rate=0.05)
        print("Initial:", account)

        # Deposit
        account.deposit(250.0)
        assert abs(account.get_balance() - 1250.0) < 1e-9
        print("After deposit:", account)

        # Withdraw
        account.withdraw(300.0)
        assert abs(account.get_balance() - 950.0) < 1e-9
        print("After withdrawal:", account)

        # Interest calculation
        interest_30 = account.calc_interest(30)
        expected_interest = 950.0 * 0.05 * (30.0 / 365.0)
        assert abs(interest_30 - expected_interest) < 1e-9
        print(f"Interest for 30 days: ${interest_30:,.2f}")

        # Change rate
        account.set_interest_rate(0.02)
        assert abs(account.interest_rate - 0.02) < 1e-9
        print("After rate change:", account)

        print("All tests passed.")

    # Run the test function
    test_bankacct()

if __name__ == "__main__":
    main()