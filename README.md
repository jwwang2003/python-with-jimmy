# Python Exercises

Practice-focused exercises paired with a lightweight autograder and answer key.

## Table of Contents

- [Python Exercises](#python-exercises)
  - [Table of Contents](#table-of-contents)
  - [Running the Exercises](#running-the-exercises)
    - [Helper script](#helper-script)
    - [Manual commands (DO NOT USE)](#manual-commands-do-not-use)
  - [Exercises](#exercises)
    - [Recursion: Fibonacci Numbers (fib)](#recursion-fibonacci-numbers-fib)
    - [Intro to Classes: BankAccount](#intro-to-classes-bankaccount)

## Running the Exercises

All commands are run from the repo root. Ensure you are using Python 3.11+.

### Helper script

Use the provided `run_assignment.sh` script to run student code, the autograder,
or the answer demo for any assignment. The script automatically sets `PYTHONPATH`
so imports work when invoked from the shell.

```bash
# Syntax
./run <assignment_name> <test|grade|demo>

# Examples
./run fib test    # run Fibonacci recursion student module
./run fib grade   # run official autograder
./run fib demo    # run the answer/demo script
./run bank test   # run bank student module (local tests)
./run bank grade  # run official autograder
./run bank demo   # run the answer/demo script
```

If needed, make the script executable once:

```bash
chmod +x run
```

### Manual commands (DO NOT USE)

You can run the same targets without the helper script:

```bash
PYTHONPATH=. python -m exercises.student.student_bank
PYTHONPATH=. python -m grade.run_bank_autograder
PYTHONPATH=. python answer/bank.py
```

## Exercises

### Recursion: Fibonacci Numbers (fib)

- **Student starter**: [`exercises/student/fib/main.py`](exercises/student/fib/main.py)
- **Reference grader**: `exercises/reference/fib.py`
- **Answer/demo**: `answer/fib.py`

Write a recursive `fib_recursive` function and print a small Fibonacci sequence.

### Intro to Classes: BankAccount

- **Student starter**: [`exercises/student/bank/main.py`](exercises/student/bank/main.py) (click on the path to get started)
- **Reference grader**: `exercises/reference/bank.py`
- **Answer/demo**: `answer/bank.py`

Implement a `BankAccount` class, practice object instantiation.
