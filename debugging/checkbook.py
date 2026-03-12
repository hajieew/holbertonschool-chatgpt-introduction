"""
checkbook.py

A simple Python checkbook program that allows users to:
- Deposit money
- Withdraw money
- Check their current balance
The program uses error handling to prevent crashes from invalid input.
"""

class Checkbook:
    """A simple checkbook class to manage balance."""

    def __init__(self):
        """Initialize the checkbook with a zero balance."""
        self.balance = 0.0

    def deposit(self, amount):
        """
        Deposit money into the checkbook.

        Parameters:
        - amount (float): The amount to deposit.
        """
        self.balance += amount
        print(f"Deposited ${amount:.2f}")
        print(f"Current Balance: ${self.balance:.2f}")

    def withdraw(self, amount):
        """
        Withdraw money from the checkbook if sufficient funds exist.

        Parameters:
        - amount (float): The amount to withdraw.
        """
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount:.2f}")
            print(f"Current Balance: ${self.balance:.2f}")

    def get_balance(self):
        """Display the current balance."""
        print(f"Current Balance: ${self.balance:.2f}")


def get_valid_amount(prompt):
    """
    Prompt the user for a numeric amount, retrying until valid.

    Parameters:
    - prompt (str): The input prompt to show.

    Returns:
    - float: A valid numeric amount entered by the user.
    """
    while True:
        try:
            amount = float(input(prompt))
            if amount < 0:
                print("Please enter a positive amount.")
            else:
                return amount
        except ValueError:
            print("Invalid input. Please enter a numeric value.")


def main():
    """Main loop for the checkbook program."""
    cb = Checkbook()
    while True:
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ").lower()
        if action == 'exit':
            print("Exiting the checkbook. Goodbye!")
            break
        elif action == 'deposit':
            amount = get_valid_amount("Enter the amount to deposit: $")
            cb.deposit(amount)
        elif action == 'withdraw':
            amount = get_valid_amount("Enter the amount to withdraw: $")
            cb.withdraw(amount)
        elif action == 'balance':
            cb.get_balance()
        else:
            print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
