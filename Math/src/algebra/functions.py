from Math.src.algebra.relation import Relation


class Function:
    def __init__(self, relation, rule=None):
        self.relation = relation
        self.is_function = relation.is_function
        self.rule = rule
        self._symmetry_type = None
        self._intervals_of_increase = None
        self._intervals_of_decrease = None
        self._monotonicity = None

    def __call__(self, x):
        if self.rule:
            return self.rule(x)
        return self.relation.get_value_from(x)

    def compose(self, other):
        pass

    def func_arithmetic(self, operand, g):
        pass

    def vertical_shift(self, k):
        def new_rule(x): return self(x) + k
        return Function(relation=self.relation, rule=new_rule)

    def horizontal_shift(self, h):
        pass

    def vertical_stretch(self, a):
        pass

    def horizontal_stretch(self, b):
        pass

    def reflect_over_x_axis(self):
        pass

    def reflect_over_y_axis(self):
        pass

    def is_even(self):
        pass

    def is_odd(self):
        pass

    def is_neither_even_nor_odd(self):
        pass

    def intervals_of_increase(self):
        pass

    def intervals_of_decrease(self):
        pass

    def is_increasing(self):
        pass

    def is_decreasing(self):
        pass

    def is_constant(self):
        pass

    def symmetry_type(self):
        return True

    # is_bounded
    # is_bounded_above
    # is_bounded_below
    # upper_bound
    # lower_bound (if exists)
    # end_behavior_right
    # end_behavior_left
