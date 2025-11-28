# assignment_triangle.py

import random
from typing import Any, Union

Number = Union[int, float]


class AssignmentTriangle:
    name = "Classes: Triangle Area"
    num_tests = 16

    def generate_input(self, rng: random.Random) -> dict[str, Number]:
        """
        Generate a random base and height.
        """
        base = rng.randint(1, 20)
        height = rng.randint(1, 20)
        return {"base": base, "height": height}

    def reference_solution(self, inp: dict[str, Number]) -> Number:
        """
        Compute triangle area using base and height.
        """
        return 0.5 * inp["base"] * inp["height"]

    def compare_outputs(self, ref: Any, student: Any) -> bool:
        """
        Compare numeric outputs with small tolerance.
        """
        try:
            ref_val = float(ref)
            stud_val = float(student)
        except (TypeError, ValueError):
            return False
        return abs(ref_val - stud_val) < 1e-6

    def format_input_for_stdin(self, inp: dict[str, Number]) -> str:
        return f"{inp['base']} {inp['height']}\n"

    def parse_output_from_stdout(self, raw: str) -> Any:
        return float(raw.strip().splitlines()[-1])
