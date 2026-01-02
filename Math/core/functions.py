"""
functions.py

Defines the Function class and related utilities for representing and manipulating mathematical functions.

This module provides:
- The Function class, which extends the Relation class to enforce the function property (each x maps to exactly one y).
- Methods for evaluating, transforming, and analyzing mathematical functions.
- Support for function composition, reflection, and other algebraic operations.

Intended for use in symbolic mathematics, algebraic manipulation, and educational tools.
"""
from typing import Optional, Callable, Any
from .relation import Relation


class Function:
    """Represents a mathematical function, built on a Relation, with optional transformation rules and analysis methods."""

    def __init__(self, relation: Relation, rule: Optional[Callable] = None):
        """
        Initialize a Function object.

        Args:
            relation (Relation): The underlying relation representing the function.
            rule (callable, optional): A callable rule for evaluating the function. Defaults to None.
        """
        if not relation.is_function:
            raise ValueError("Relation is not a function")

        self.relation = relation
        self.rule = rule
        self._symmetry_type = None
        self._intervals_of_increase = None
        self._intervals_of_decrease = None
        self._monotonicity = None

    def __call__(self, x: Any):
        """
        Evaluate the function at a given input x.

        Args:
            x: The input value.
        Returns:
            The output of the function for input x.
        """
        if self.rule:
            return self.rule(x)
        return self.relation.get_value_for(x)

    @property
    def return_symmetry_type(self):
        """Returns attribute of symmetry type from object"""
        return self._symmetry_type

    @staticmethod
    def identity(range_start=0, range_end=1):
        """
        Create an identity function $f(x) = x$ over a specified domain.

        Args:
            range_start (int): Start of the domain (inclusive).
            range_end (int): End of the domain (exclusive).
        Returns:
            Function: The identity function.
        """
        return Function(relation=Relation([(x, x) for x in range(range_start, range_end)]), rule=lambda x: x)

    @staticmethod
    def constant(c=0, range_start=0, range_end=1):
        """
        Create a constant function $f(x) = c$ over a specified domain.

        Args:
            c: The constant value to return.
            range_start (int): Start of the domain (inclusive).
            range_end (int): End of the domain (exclusive).
        Returns:
            Function: The constant function.
        """
        return Function(relation=Relation([(x, c) for x in range(range_start, range_end)]), rule=lambda x: c)

    def compose(self, other):
        """Return the composition of this function with another function.

        Args:
            other (Function): The inner function to compose with.
        Returns:
            Function: The composed function f(g(x))."""
        return Function(relation=self.relation, rule=lambda x: self(other(x)))

    def func_arithmetic(self, operand, g):
        """
        Perform an arithmetic operation with another function g (not implemented).

        Args:
            operand (str): The arithmetic operation ('+', '-', '*', '/').
            g (Function): The other function.
        """

    def vertical_shift(self, k):
        """
        Return a new Function shifted vertically by k units.

        Args:
            k: The amount to shift vertically.
        Returns:
            Function: The vertically shifted function.
        """
        return Function(relation=self.relation, rule=lambda x: self(x) + k)

    def horizontal_shift(self, h):
        """
        Return a new Function shifted horizontally by h units.

        Args:
            h: The amount to shift horizontally.
        Returns:
            Function: The horizontally shifted function.
        """
        return Function(relation=self.relation, rule=lambda x: self(x - h))

    def vertical_stretch(self, a):
        """
        Return a new Function stretched vertically by a factor of a.

        Args:
            a: The vertical stretch factor.
        Returns:
            Function: The vertically stretched function.
        """
        return Function(relation=self.relation, rule=lambda x: self(x) * a)

    def horizontal_stretch(self, b):
        """
        Return a new Function stretched horizontally by a factor of b.

        Args:
            b: The horizontal stretch factor.
        Returns:
            Function: The horizontally stretched function.
        """
        return Function(relation=self.relation, rule=lambda x: self(x * b))

    def reflect_over_x_axis(self) -> 'Function':
        """
        Return a new Function reflected over the x-axis.

        Returns:
            Function: The function reflected over the x-axis ($f(x) \to -f(x)$).
        """
        return Function(relation=self.relation, rule=lambda x: -self(x))

    def reflect_over_y_axis(self) -> "Function":
        """
        Return a new Function reflected over the y-axis.

        Returns:
            Function: The function reflected over the y-axis ($f(x) \to f(-x)$).
        """
        return Function(relation=self.relation, rule=lambda x: self(-x))

    def check_symmetry(self) -> None:
        """
        Check and set self._symmerty_type whether the function is even, odd, or neither.
        Compares f(x) to f(-x) and -f(x) for all x in the domain.
        """

        if all(self(x) == self.reflect_over_y_axis()(x) for x in self.relation.domain):
            self._symmetry_type = 'even'
        elif all(self.reflect_over_y_axis()(x) == -self(x) for x in self.relation.domain):
            self._symmetry_type = 'odd'
        else:
            self._symmetry_type = 'neither'

    def intervals_of_increase(self):
        """
        Return intervals where the function is increasing (not implemented).
        """

    def intervals_of_decrease(self):
        """
        Return intervals where the function is decreasing (not implemented).
        """

    def is_increasing(self):
        """
        Check if the function is increasing (not implemented).
        """

    def is_decreasing(self):
        """
        Check if the function is decreasing (not implemented).
        """

    def is_constant(self):
        """
        Check if the function is constant (not implemented).
        """

    def symmetry_type(self):
        """
        Return the symmetry type of the function (not implemented).
        """
        return True

    # is_bounded
    # is_bounded_above
    # is_bounded_below
    # upper_bound
    # lower_bound (if exists)
    # end_behavior_right
    # end_behavior_left
