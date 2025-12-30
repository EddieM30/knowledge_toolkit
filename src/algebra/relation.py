import random


class Relation:
    """Instantiates an instance of a Relation -- the Parent class to functions"""

    def __init__(self, pairs=None):
        self.pairs = set(pairs) if pairs else set()

    @property
    def domain(self):
        """Returns unique x values in set, ignores duplicates"""
        return {pair[0] for pair in self.pairs}

    @property
    def range(self):
        """Returns unique y values in set, ignores duplicates"""
        return {pair[1] for pair in self.pairs}

    @property
    def inverse(self):
        """Returns new instance of class Relation with inversed pairs"""
        return Relation([pair[::-1] for pair in self.pairs])

    @property
    def is_function(self):
        """The Vertical line test: Does each x have exactly one y?"""
        return len(self.domain) == len(self.pairs)

    @property
    def is_one_to_one(self):
        """The Horizontal Line Test: Does each y have exactly one x?"""
        return len(self.range) == len(self.pairs)
