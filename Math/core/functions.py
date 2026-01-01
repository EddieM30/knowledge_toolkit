from .relation import Relation


class Function:
    """Represents a mathematical function, built on a Relation, with optional transformation rules and analysis methods."""

    def __init__(self, relation, rule=None):
        """Initialize a Function with a Relation and an optional rule (callable)."""
        self.relation = relation
        self.is_function = relation.is_function
        self.rule = rule
        self._symmetry_type = None
        self._intervals_of_increase = None
        self._intervals_of_decrease = None
        self._monotonicity = None

    def __call__(self, x):
        """Evaluate the function at a given input x."""
        if self.rule:
            return self.rule(x)
        return self.relation.get_value_from(x)

    def compose(self, other):
        """Return the composition of this function with another function """
        def h(x): return self(other(x))
        return Function(relation=self.relation, rule=h)

    def func_arithmetic(self, operand, g):
        """Perform arithmetic operation with another function g (not implemented)."""
        pass

    def vertical_shift(self, k):
        """Return a new Function shifted vertically by k units."""
        def new_rule(x): return self(x) + k
        return Function(relation=self.relation, rule=new_rule)

    def horizontal_shift(self, h):
        """Return a new Function shifted horizontally by h units (not implemented)."""
        pass

    def vertical_stretch(self, a):
        """Return a new Function stretched vertically by a factor of a (not implemented)."""
        pass

    def horizontal_stretch(self, b):
        """Return a new Function stretched horizontally by a factor of b (not implemented)."""
        pass

    def reflect_over_x_axis(self):
        """Return a new Function reflected over the x-axis (not implemented)."""
        pass

    def reflect_over_y_axis(self):
        """Return a new Function reflected over the y-axis (not implemented)."""
        pass

    def is_even(self):
        """Check if the function is even (not implemented)."""
        pass

    def is_odd(self):
        """Check if the function is odd (not implemented)."""
        pass

    def is_neither_even_nor_odd(self):
        """Check if the function is neither even nor odd (not implemented)."""
        pass

    def intervals_of_increase(self):
        """Return intervals where the function is increasing (not implemented)."""
        pass

    def intervals_of_decrease(self):
        """Return intervals where the function is decreasing (not implemented)."""
        pass

    def is_increasing(self):
        """Check if the function is increasing (not implemented)."""
        pass

    def is_decreasing(self):
        """Check if the function is decreasing (not implemented)."""
        pass

    def is_constant(self):
        """Check if the function is constant (not implemented)."""
        pass

    def symmetry_type(self):
        """Return the symmetry type of the function (not implemented)."""
        return True

    # is_bounded
    # is_bounded_above
    # is_bounded_below
    # upper_bound
    # lower_bound (if exists)
    # end_behavior_right
    # end_behavior_left
