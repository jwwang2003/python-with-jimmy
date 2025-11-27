# student_fib.py

from typing import Dict

TestCase = Dict[str, int]


def fib_recursive(n: int) -> int:
    """
    Return the nth Fibonacci number using recursion.
    fib(0) = 0
    fib(1) = 1
    fib(n) = fib(n-1) + fib(n-2) for n >= 2
    """
    # TODO 1: Handle the base cases.
    # - if n == 0, return 0
    # - if n == 1, return 1

    # TODO 2: Handle the recursive case.
    # - for n >= 2, return fib_recursive(n - 1) + fib_recursive(n - 2)

    # (Optional) TODO 3: You can guard against negative input by raising
    # a ValueError if n < 0.
    pass


if __name__ == "__main__":
    # ---------- Part 2: Using the function ----------

    # TODO 4: Pick a value for 'target_n' (for example, 8 or 10).
    target_n =                  # Fill in here!

    # TODO 5: Print the nth Fibonacci number using your recursive function.
    print(f"Fib({target_n}) = {fib_recursive(target_n)}")

    # TODO 6: Print the sequence from Fib(0) up to Fib(target_n).
    sequence = [fib_recursive(i) for i in range(target_n + 1)]
    print("Sequence:", sequence)


# DO NOT MODIFY ANY CODE BELOW THIS POINT

def solve(test_case: TestCase) -> int:
    """
    test_case is a dict: {"n": int}
    Return fib_recursive(n).
    """
    n_value = test_case["n"]
    return fib_recursive(n_value)
