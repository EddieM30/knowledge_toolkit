from typing import Callable, Any
from Math.core.functions import Function

'''
You should validate there are at least two distinct points.
Detect vertical segments (x2 == x1) and raise; a vertical line is not a function in y = mx + b form.
Avoid dividing by zero in slope calculation.

Logic bugs / ordering


Numeric robustness

Use math.isclose when comparing floating-point slopes rather than exact equality.
Consider sorting points by x before computing slopes so the order is predictable (and to avoid issues if input isn't sorted).
API / typing / usability

Use Optional[Callable[..., Any]] for rule if you need Python <3.10 compatibility; your union style is fine on 3.10+.
Compute and store the y-intercept (b) during init so subsequent calls don't rely on a separate method call.
Provide a safe call implementation that falls back to the linear formula if rule is None.
Minor

Add docstrings, repr or str for debugging, and small unit / usage examples.'''


class LinearFunction(Function):
    def __init__(self, slope, y_intercept):
        self.m = float(slope)
        self.b = float(y_intercept)
        def rule(x): return self.m * x + self.b
        super().__init__(rule=rule)

    @classmethod
    def from_points(cls, points: list[tuple[float, float]]):
        if len(points) < 2:
            raise ValueError('At least two points required')

        unique_points = sorted(set(points), key=lambda p: p[0])
        if len(unique_points) < 2:
            raise ValueError('At least 2 distint points required.')

        x1, y1 = unique_points[0]
        x2, y2 = unique_points[1]
        if x2 - x1 == 0:
            raise ValueError('Vertical line - not a function')
        m = (y2 - y1) / (x2 - x1)
        b = y1 - m * x1

        for x, y in unique_points:
            if abs(y - (m * x + b)) > 1e-10:
                raise ValueError(
                    'Points are not colinear -- cannot form a linear function.')

        return cls(slope=m, y_intercept=b)

    @property
    def y_intercept(self):
        """Returns y_intercept"""
        return self.b

    @property
    def x_intercept(self):
        """Computed from self.m and self.b"""
        return -self.b / self.m if self.m != 0 else None

    @property
    def pretty_equation(self):
        """Returns a pretty string equation computed with self.m and self.b"""
        pass

    def intersect_with(self, other):
        """Determines if two Linear Functions intersect with each other"""
        pass

    def is_parallel_to(self, other):
        """Determines if two linear functions are parallel to each other"""
        pass

    def is_perpendicular_to(self, other):
        """Determines if two linear functions are perpendicular to each other"""
        pass

    def solve_for_x(self, y_value):
        """Rearranges y = mx + b -> x = (y - b) / m"""
        pass

    def y_value(self, x):
        """"""
        pass

    def point_on_line(self, x):
        """Returns x, y based off of x"""
        pass

    def distance_from_point(self, point):
        """Uses the point to line distance formula with self.m and self.b"""
        pass
