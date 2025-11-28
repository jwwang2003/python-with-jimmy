# run_triangle_autograder.py

from autograder import GradingConfig, grade_function_based
from exercises.reference.triangle import AssignmentTriangle


if __name__ == "__main__":
    assignment = AssignmentTriangle()
    config = GradingConfig(
        student_module="exercises.student.triangle.main",
        student_function="solve",
        seed=202,
    )
    grade_function_based(assignment, config)
