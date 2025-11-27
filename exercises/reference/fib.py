# assignment_fib.py

import random
from typing import Any


class AssignmentFibonacci:
    name = "Recursion: Fibonacci Numbers"
    num_tests = 16

    def generate_input(self, rng: random.Random) -> int:
        """
        Generate a random non-negative integer for Fibonacci.
        Keep the numbers modest to avoid huge recursion depth.
        """
        return rng.randint(0, 15)

    def reference_solution(self, n: int) -> int:
        """
        Recursive reference implementation of fib(n).
        """
        if n < 0:
            raise ValueError("n must be non-negative")
        if n in (0, 1):
            return n
        return self.reference_solution(n - 1) + self.reference_solution(n - 2)

    def compare_outputs(self, ref: Any, student: Any) -> bool:
        """
        Compare integer outputs, allowing ints/strings that cast cleanly.
        """
        try:
            return int(ref) == int(student)
        except (TypeError, ValueError):
            return False

    def format_input_for_stdin(self, inp: int) -> str:
        return f"{inp}\n"

    def parse_output_from_stdout(self, raw: str) -> Any:
        return int(raw.strip().splitlines()[-1])
