"""
autograder.py

Generic template for autograding Python labs/projects.

You define:
- an Assignment subclass with:
    - generate_input()
    - reference_solution()
    - compare_outputs()
- how to load/execute the student's code:
    - as a Python function in a module
    - or as a standalone script (via subprocess)

Then run this file to grade.
"""

import importlib
import random
import subprocess
import sys
from dataclasses import dataclass
from typing import Any, Tuple, Protocol


# ---------- Assignment interface ----------

class Assignment(Protocol):
    """
    Protocol (interface) for an assignment.

    You create a class implementing these methods
    for each lab/project you want to autograde.
    """

    name: str
    num_tests: int

    def generate_input(self, rng: random.Random) -> Any:
        """
        Return a single random test input (any Python object).
        Example: an int, tuple, dict, etc.
        """
        ...

    def reference_solution(self, inp: Any) -> Any:
        """
        Given the input, compute the correct output using
        your official/standard solution.
        """
        ...

    def compare_outputs(self, ref: Any, student: Any) -> bool:
        """
        Return True if the student's output is correct enough.
        You can allow small numeric tolerances, order-insensitive
        comparisons, etc.
        """
        ...

    # ---- OPTIONAL: for script-based grading ----

    def format_input_for_stdin(self, inp: Any) -> str:
        """
        Convert `inp` to the text that should be sent to the student's
        program via stdin. Default: just `str(inp)` plus newline.
        """
        return str(inp) + "\n"

    def parse_output_from_stdout(self, raw: str) -> Any:
        """
        Parse the student's text output back into a Python value to compare
        with the reference solution.
        Default: strip whitespace and return the raw string.
        """
        return raw.strip()


# ---------- Configuration for grading ----------

@dataclass
class GradingConfig:
    # For function-based grading:
    student_module: str = "student_solution"  # e.g. 'lab1_solution'
    student_function: str = "solve"           # the function to call

    # For script-based grading:
    student_script: str = "student_solution.py"  # path to script
    python_executable: str = sys.executable      # usually fine as-is

    # General:
    seed: int = 42  # RNG seed for reproducibility


# ---------- Console helpers ----------

RESET = "\033[0m"
COLORS = {
    "green": "\033[92m",
    "red": "\033[91m",
    "yellow": "\033[93m",
    "blue": "\033[94m",
    "bold": "\033[1m",
}


def supports_color() -> bool:
    """
    Return True when stdout supports ANSI colors.
    """
    return sys.stdout.isatty()


def stylize(text: str, color_key: str) -> str:
    """
    Wrap the text in ANSI escape codes when supported.
    """
    if not supports_color():
        return text
    color = COLORS.get(color_key, "")
    if not color:
        return text
    return f"{color}{text}{RESET}"


def print_banner(title: str):
    """
    Print a simple boxed banner for section titles.
    """
    line = "=" * (len(title) + 4)
    print(line)
    print(f"| {title} |")
    print(line)


def render_status(label: str) -> str:
    """
    Return a formatted status badge for PASS/FAIL/CRASH.
    """
    palette = {
        "PASS": "green",
        "FAIL": "red",
        "CRASH": "yellow",
    }
    color = palette.get(label, "blue")
    return stylize(f"[ {label:^5} ]", color)


def render_progress_bar(passed: int, total: int) -> str:
    """
    Return an ASCII progress bar summarizing the score.
    """
    width = 26
    ratio = passed / total if total else 0
    filled = int(ratio * width)
    bar = "=" * filled + "-" * (width - filled)
    return f"[{bar}] {ratio * 100:5.1f}%"


def print_test_block(test_num: int, status: str, inp: Any,
                     ref_out: Any, stud_out: Any):
    """
    Pretty-print the result of a single test case.
    """
    header = f"Test {test_num:02d}"
    print(f"{render_status(status)} {stylize(header, 'bold')}")
    print(f"    Input     : {inp!r}")
    print(f"    Reference : {ref_out!r}")
    print(f"    Student   : {stud_out!r}")
    print("-" * 60)


# ---------- Helpers to load/execute student code ----------

def load_student_function(module_name: str, func_name: str):
    """
    Dynamically import the student's module and get the target function.
    """
    module = importlib.import_module(module_name)
    func = getattr(module, func_name, None)
    if func is None:
        raise AttributeError(
            f"Module '{module_name}' has no function '{func_name}'"
        )
    return func


def run_student_script(config: GradingConfig, assignment: Assignment, inp: Any) -> Any:
    """
    Run student's program as a separate Python process that communicates
    via stdin/stdout.

    Expects the program to read from stdin and print the answer to stdout.
    """
    text_input = assignment.format_input_for_stdin(inp)

    proc = subprocess.Popen(
        [config.python_executable, config.student_script],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )

    stdout, stderr = proc.communicate(text_input)

    if proc.returncode != 0:
        raise RuntimeError(
            f"Student script exited with code {proc.returncode}.\n"
            f"stderr:\n{stderr}"
        )

    return assignment.parse_output_from_stdout(stdout)


# ---------- Grading logic ----------

def grade_function_based(assignment: Assignment, config: GradingConfig):
    """
    Grade a student function of the form:
        def solve(input):
            ...
            return output
    """
    rng = random.Random(config.seed)
    student_func = load_student_function(config.student_module,
                                         config.student_function)

    total = assignment.num_tests
    passed = 0

    print_banner(f"{assignment.name} · Function Mode")
    print()

    for i in range(1, total + 1):
        inp = assignment.generate_input(rng)
        ref_out = assignment.reference_solution(inp)
        status = "FAIL"

        try:
            stud_out = student_func(inp)
        except Exception as e:
            stud_out = f"{e.__class__.__name__}: {e}"
            status = "CRASH"
        else:
            ok = assignment.compare_outputs(ref_out, stud_out)
            if ok:
                passed += 1
                status = "PASS"
            else:
                status = "FAIL"

        print_test_block(i, status, inp, ref_out, stud_out)

    print(render_progress_bar(passed, total))
    print(f"Score: {passed}/{total} tests passed")


def grade_script_based(assignment: Assignment, config: GradingConfig):
    """
    Grade a student *script* that reads from stdin and writes to stdout.
    """
    rng = random.Random(config.seed)
    total = assignment.num_tests
    passed = 0

    print_banner(f"{assignment.name} · Script Mode")
    print()

    for i in range(1, total + 1):
        inp = assignment.generate_input(rng)
        ref_out = assignment.reference_solution(inp)
        status = "FAIL"

        try:
            stud_out = run_student_script(config, assignment, inp)
        except Exception as e:
            stud_out = f"{e.__class__.__name__}: {e}"
            status = "CRASH"
        else:
            ok = assignment.compare_outputs(ref_out, stud_out)
            if ok:
                passed += 1
                status = "PASS"
            else:
                status = "FAIL"

        print_test_block(i, status, inp, ref_out, stud_out)

    print(render_progress_bar(passed, total))
    print(f"Score: {passed}/{total} tests passed")


# ---------- Example usage entrypoint ----------

if __name__ == "__main__":
    # Import your specific assignment class here.
    # Example: from assignment01 import Assignment01
    from assignment01 import Assignment01

    assignment = Assignment01()
    config = GradingConfig(
        student_module="student_solution",  # change per lab if needed
        student_function="solve",
        student_script="student_solution.py",
        seed=42,
    )

    # Choose ONE of these depending on your setup:
    grade_function_based(assignment, config)
    # grade_script_based(assignment, config)
