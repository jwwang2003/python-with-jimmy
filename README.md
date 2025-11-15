# Python Exercises

Practice-focused exercises paired with a lightweight autograder and answer key.

## Table of Contents

1. [Intro to Classes: BankAccount](#intro-to-classes-bankaccount)
2. [Running the Exercises](#running-the-exercises)

## Intro to Classes: BankAccount

- **Student starter**: `exercises/student/student_bank.py`
- **Reference grader**: `exercises/reference/bank.py`
- **Answer/demo**: `answer/bank.py`

Students implement a `BankAccount` class, practice object instantiation, and then
finish a `solve()` helper that powers the autograder tests.

## Running the Exercises

All commands are run from the repo root. Ensure you are using Python 3.11+.

### Helper script

Use the provided `run_assignment.sh` script to run student code, the autograder,
or the answer demo for any assignment. The script automatically sets `PYTHONPATH`
so imports work when invoked from the shell.

```bash
# Syntax
./run_assignment.sh <assignment_name> <test|grade|demo>

# Examples for the Bank assignment
./run_assignment.sh bank test   # run student module (local tests)
./run_assignment.sh bank grade  # run official autograder
./run_assignment.sh bank demo   # run the answer/demo script
```

If needed, make the script executable once:

```bash
chmod +x run_assignment.sh
```

### Manual commands

You can run the same targets without the helper script:

```bash
PYTHONPATH=. python -m exercises.student.student_bank
PYTHONPATH=. python -m grade.run_bank_autograder
PYTHONPATH=. python answer/bank.py
```
