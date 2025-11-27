# run_fib_autograder.py

from autograder import GradingConfig, grade_function_based
from exercises.reference.fib import AssignmentFibonacci


if __name__ == "__main__":
    assignment = AssignmentFibonacci()
    config = GradingConfig(
        student_module="exercises.student.fib.main",
        student_function="solve",
        seed=101,
    )
    grade_function_based(assignment, config)
