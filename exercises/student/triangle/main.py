# student_triangle.py

from typing import Dict, Union

Number = Union[int, float]
TestCase = Dict[str, Number]


class Triangle:
    """
    Simple triangle defined by base and height.
    Area = 0.5 * base * height
    """

    # TODO 1: Implement __init__(self, base, height)
    # - store base and height as attributes on self
    # - you may want to type-hint them as Number
    def __init__(self, base: Number, height: Number):
        # your code here
        pass

    # TODO 2: Implement area(self) -> Number
    # - return 0.5 * self.base * self.height
    def area(self) -> Number:
        # your code here
        pass

    # TODO 3: Override __str__(self) -> str
    # - return a helpful summary string, e.g.
    #   "Triangle(base=3, height=4, area=6.0)"
    def __str__(self) -> str:
        # your code here
        pass


if __name__ == "__main__":
    # ---------- Part 2: Using the class ----------

    # TODO 4: Create an example triangle (choose any base/height, e.g., 3 and 4).
    example =                      # Fill in here!

    # TODO 5: Print its area using the area method.
    print("Area:", ...)

    # TODO 6: Print the object itself (this should call __str__).
    print(...)


# DO NOT MODIFY ANY CODE BELOW THIS POINT

def solve(test_case: TestCase) -> Number:
    """
    test_case is a dict: {"base": Number, "height": Number}
    Return the triangle area.
    """
    tri = Triangle(test_case["base"], test_case["height"])
    return tri.area()
