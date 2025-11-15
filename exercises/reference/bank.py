# assignment_bankaccount.py

import random
from typing import Any, Dict, List, Tuple

# Test-case type:
# {
#     "starting_balance": int,
#     "ops": List[Tuple[str, int]]   # [("deposit", 50), ("withdraw", 20), ...]
# }

class AssignmentBankAccount:
    name = "Intro to Classes: BankAccount"
    num_tests = 20

    def generate_input(self, rng: random.Random) -> Dict[str, Any]:
        """
        Generate a random test case:
        - random starting balance
        - random sequence of deposit/withdraw operations
        """
        starting_balance = rng.randint(0, 500)

        num_ops = rng.randint(1, 8)
        ops: List[Tuple[str, int]] = []
        for _ in range(num_ops):
            kind = rng.choice(["deposit", "withdraw"])
            amount = rng.randint(1, 300)
            ops.append((kind, amount))

        return {
            "starting_balance": starting_balance,
            "ops": ops,
        }

    def reference_solution(self, inp: Dict[str, Any]) -> int:
        """
        Pure-data reference implementation of the BankAccount logic.
        Withdraws only if there is enough money.
        Returns the final balance.
        """
        balance = inp["starting_balance"]
        for kind, amount in inp["ops"]:
            if kind == "deposit":
                balance += amount
            elif kind == "withdraw":
                if balance >= amount:
                    balance -= amount
        return balance

    def compare_outputs(self, ref: Any, student: Any) -> bool:
        """
        Compare the reference final balance with the student's final balance.
        """
        try:
            return int(ref) == int(student)
        except (TypeError, ValueError):
            return False

    # Only needed if you want script-based grading (stdin/stdout):
    def format_input_for_stdin(self, inp: Dict[str, Any]) -> str:
        # Simple text format:
        # starting_balance
        # num_ops
        # kind amount
        # kind amount ...
        lines = []
        lines.append(str(inp["starting_balance"]))
        lines.append(str(len(inp["ops"])))
        for kind, amount in inp["ops"]:
            lines.append(f"{kind} {amount}")
        return "\n".join(lines) + "\n"

    def parse_output_from_stdout(self, raw: str) -> Any:
        # Expect the student to print just the final balance
        return int(raw.strip().splitlines()[-1])