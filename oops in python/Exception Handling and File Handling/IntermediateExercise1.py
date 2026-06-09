# Custom Exception
class LowBalanceError(Exception):
    def __init__(self, message="Withdrawal denied! Balance cannot go below 1000 units."):
        super().__init__(message)


# Function to perform withdrawal
def withdraw(balance, amount):
    if balance - amount < 1000:
        raise LowBalanceError()  # Raise custom exception
    balance -= amount
    print(f"Withdrawal successful! New balance: {balance}")
    return balance


# Example usage
if __name__ == "__main__":
    balance = 1500  # Current account balance
    amount_to_withdraw = 600  # Amount to withdraw

    try:
        balance = withdraw(balance, amount_to_withdraw)
    except LowBalanceError as e:
        print(f"Error: {e}")
