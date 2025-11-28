# Reference answer for triangle.py

from typing import Dict, Union

Number = Union[int, float]
TestCase = Dict[str, Number]


class Triangle:
    """
    Simple triangle defined by base and height.
    Area = 0.5 * base * height
    """

    def __init__(self, base: Number, height: Number):
        self.base: Number = base
        self.height: Number = height

    def area(self) -> Number:
        return 0.5 * self.base * self.height

    def __str__(self) -> str:
        return f"Triangle(base={self.base}, height={self.height}, area={self.area()})"


if __name__ == "__main__":
    # ---------- Part 2: Using the class ----------

    example = Triangle(3, 4)
    print("Area:", example.area())
    print(example)


# DO NOT MODIFY ANY CODE BELOW THIS POINT

def solve(test_case: TestCase) -> Number:
    """
    test_case is a dict: {"base": Number, "height": Number}
    Return the triangle area.
    """
    tri = Triangle(test_case["base"], test_case["height"])
    return tri.area()
