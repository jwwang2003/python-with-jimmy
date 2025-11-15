# student_bank.py

# ---------- Part 1: Defining the class ----------

from typing import Dict, List, Tuple, Union

Money = Union[int, float]
Operation = Tuple[str, Money]
TestCase = Dict[str, Union[Money, List[Operation]]]

class BankAccount:
    # TODO 1: Add an __init__ method that:
    # - takes 'owner' (str) and 'starting_balance' (float or int, default 0)
    # - stores them as attributes self.owner and self.balance
    #   - Hint (to store into a variable inside of the class): self.owner = owner 
    # Hint: def __init__(self, owner, starting_balance=0):
    # Use simple assignment statements.
    def __init__(self, owner: str, starting_balance: Money = 0):
        # store owner
        # store starting balance
        
        # DO NOT MODIFY BELOW
        pass

    # TODO 2: Add a deposit method
    # - takes 'amount'
    # - increases self.balance by amount
    # - does not return anything
    # Use addition + assignment.
    def deposit(self, amount: Money) -> None:
        # your code here
        
        # DO NOT MODIFY BELOW
        pass

    # TODO 3: Add a withdraw method
    # - takes 'amount'
    # - if there is enough money (self.balance >= amount),
    #   subtract from balance and return True
    # - otherwise, do NOT change balance and return False
    # Use an if statement and return True/False.
    def withdraw(self, amount: Money) -> bool:
        # your code here
        
        # DO NOT MODIFY BELOW
        pass

    # TODO 4: Add a method get_summary that returns a string like:
    # "Owner: Alice, Balance: 120.0"
    # Return an f-string that includes owner and balance.
    def get_summary(self) -> str:
        # your code here
        
        # DO NOT MODIFY BELOW
        pass

if __name__ == "__main__":
    # ---------- Part 2: Using the class ----------

    # TODO 5: Create two BankAccount objects:
    # - account1 with owner "Alice" and starting_balance 100
    # - account2 with owner "Bob" and starting_balance 50
    # Hint: account1 = BankAccount("Alice", 100)
    account1 =                  # Fill in here!
    account2 =                  # Fill in here!

    # TODO 6: Call deposit and withdraw methods:
    # - deposit 25 into Alice's account
    # - withdraw 10 from Bob's account    
    # Fill in here! [Start]

    # [End]
    
    # TODO 7: Print summaries for BOTH accounts using the built-in method get_summary()
    print(...)
    print(...)

    # (Optional) TODO 8: Try to withdraw 1,000,000 from Alice's account and
    # print whether it worked, and the final summary.
    success = account1.withdraw(...)
    print("Was large withdrawal successful?", success)
    print(...)


# DO NOT MODIFY ANY CODE BELOW THIS POINT

def solve(test_case: TestCase) -> Money:
    """
    test_case is a dict:
        {
            "starting_balance": int,
            "ops": [("deposit", 50), ("withdraw", 20), ...]
        }
    Return final balance (int or float).
    """
    starting_balance = test_case["starting_balance"]
    ops = test_case["ops"]

    acc = BankAccount("TestUser", starting_balance)

    for kind, amount in ops:
        if kind == "deposit":
            acc.deposit(amount)
        elif kind == "withdraw":
            acc.withdraw(amount)

    return acc.balance
