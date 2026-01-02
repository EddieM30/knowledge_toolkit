"""
relation.py

Defines the Relation class and related utilities for representing mathematical relations.
"""
from typing import List, Tuple, Any, Optional, Set


class Relation:
    """Instantiates an instance of a Relation -- the Parent class to functions"""

    def __init__(self, pairs: Optional[List[Tuple[Any, Any]]] = None):
        self.pairs: Set[Tuple[Any, Any]] = set(pairs) if pairs else set()

    def get_value_for(self, x_input: Any) -> Any:
        """Return the first y output corresponding with x_input.

        Args:
            x_input (val): one of the x values within the set of this relation.
        Returns: 
            The first of y values corresponding with x_input y1."""
        try:
            for x, y in self.pairs:
                if x == x_input:
                    return y
        except Exception as exc:
            raise ValueError(
                f"Value {x_input} not found in the domain of this relation") from exc

    def get_all_values_for(self, x_input: Any) -> Set:
        """Return the set of y outputs corresponding with x_input.

        Args:
            x_input (val): one of the x values within the set of this relation.
        Returns: 
            Set of y values corresponding with x_input {y1, y2, y3}."""
        y_vals = []
        try:
            for x, y in self.pairs:
                if x == x_input:
                    y_vals.append(y)
            return set(y_vals)
        except Exception as exc:
            raise ValueError(
                f"Value {x_input} not found in the domain of this relation") from exc

    @property
    def domain(self) -> Set:
        """Returns unique x values in set, ignores duplicates"""
        return {pair[0] for pair in self.pairs}

    @property
    def range(self) -> Set:
        """Returns unique y values in set, ignores duplicates"""
        return {pair[1] for pair in self.pairs}

    @property
    def inverse(self) -> "Relation":
        """Returns new instance of class Relation with inversed pairs"""
        return Relation([pair[::-1] for pair in self.pairs])

    @property
    def is_function(self) -> bool:
        """The Vertical line test: Does each x have exactly one y?"""
        return len(self.domain) == len(self.pairs)

    @property
    def is_one_to_one(self) -> bool:
        """The Horizontal Line Test: Does each y have exactly one x?"""
        return len(self.range) == len(self.pairs)
