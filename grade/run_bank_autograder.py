# run_bank_autograder.py

from autograder import grade_function_based, GradingConfig
from exercises.reference.bank import AssignmentBankAccount

if __name__ == "__main__":
    assignment = AssignmentBankAccount()
    config = GradingConfig(
        student_module="exercises.student.bank.main",  # <-- student's file name (without .py)
        student_function="solve",
        seed=69,
    )
    grade_function_based(assignment, config)
