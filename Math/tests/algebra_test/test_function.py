import pytest
from Math.core.functions import Function
from Math.core.relation import Relation

functional_rel = Relation([(x, x**2) for x in range(-5, 6)])
non_function_rel = Relation([(1, 2), (2, 3), (1, 5)])


def test_is_function_on_instantiation():
    """
    Test that a Function instantiated with a functional Relation
    is recognized as a function (passes the vertical line test).
    """

    func = Function(pairs=functional_rel.pairs)
    assert func.is_function is True


def test_is_not_function_on_instantiation():
    """
        Test that a Function instantiated with a non-functional Relation
        is not recognized as a function (fails the vertical line test).
        """

    with pytest.raises(ValueError) as excinfo:
        Function(pairs=non_function_rel.pairs)
    assert "Relation is not a function" in str(excinfo.value)


def test_rule_evaluation():
    """
        Test that a Function with a rule evaluates correctly for given inputs.
        """
    f = Function(pairs=functional_rel.pairs, rule=lambda x: x**2)

    assert f(4) == 16
    assert f(5) == 25


def test_compose():
    f = Function(pairs=([(x, x**2)
                 for x in range(-5, 6)]), rule=lambda x: x**2)
    g = Function(pairs=([(x, x + 1)
                 for x in range(-5, 6)]), rule=lambda x: x + 1)

    h = f.compose(g)

    assert h(2) == 9  # (2+1)^2 = 9
    assert h(0) == 1  # (0+1)^2 = 1
    assert h(-2) == 1  # (-2+1) = 1


def test_compose_with_self():
    f = Function(pairs=([(x, x - 3)
                 for x in range(-5, 6)]), rule=lambda x: x - 3)

    h = f.compose(f)

    assert h(2) == -4
    assert h(-7) == -13
    assert h(5) == -1


def test_compose_identity():
    i = Function.identity(-5, 6)
    f = Function(pairs=([(x, x**2)
                 for x in range(-5, 6)]), rule=lambda x: x**2)
    h = f.compose(i)  # h = f(i(x))

    assert i(2) == 2
    assert h(2) == 4
    assert h(100) == 10000
    assert h(2 * (3 - 5)) == (2 * (3 - 5))**2
    assert h(2 * (3 - 5)) == 16


def test_compose_constant():
    f = Function.constant(7)

    g = Function(pairs=([(x, x**3)
                 for x in range(-5, 6)]), rule=lambda x: x**3)
    h = f.compose(g)

    assert f(1) == 7
    assert h(9) == 7


def test_check_symmetry_is_even():
    f = Function(pairs=(
        [(x, x**2) for x in range(-5, 6)]), rule=lambda x: x**2)
    f.check_symmetry()

    assert f.return_symmetry_type == 'even'


def test_check_symmetry_is_odd():
    f = Function(pairs=(
        [(x, x**3) for x in range(-5, 6)]), rule=lambda x: x**3)
    f.check_symmetry()

    assert f.return_symmetry_type == 'odd'


def test_check_symmetry_is_neither():
    f = Function(pairs=(
        [(x, x + 1) for x in range(-5, 6)]), rule=lambda x: x + 1)
    f.check_symmetry()

    assert f.return_symmetry_type == 'neither'


def test_interval_increase():
    increasing_pairs = [(1, 2), (2, 4), (3, 6), (4, 8)]
    f = Function(pairs=increasing_pairs)
    # Happy path: strictly increasing
    assert f.intervals_of_increase() == [(1, 2), (2, 3), (3, 4)]
    assert f._merge_intervals(f.intervals_of_increase()) == [(1, 4)]


def test_interval_decrease():
    decreasing_pairs = [(1, 8), (2, 6), (3, 4), (4, 2)]
    f = Function(pairs=decreasing_pairs)
    # Happy path: strictly decreasing
    assert f.intervals_of_decrease() == [(1, 2), (2, 3), (3, 4)]
    assert f._merge_intervals(f.intervals_of_decrease()) == [(1, 4)]


def test_interval_constant():
    constant_pairs = [(1, 5), (2, 5), (3, 5), (4, 5)]
    f = Function(pairs=constant_pairs)
    # Happy path: constant
    assert f.intervals_are_constant() == [(1, 2), (2, 3), (3, 4)]
    assert f._merge_intervals(f.intervals_are_constant()) == [(1, 4)]


def test_merge_overlapping_and_non_overlapping():
    pairs = [
        (1, 5), (4, 8), (7, 10), (9, 12),  # overlapping
        (13, 15), (16, 18),  # non-overlapping
        (20, 22), (23, 25),  # non-overlapping
        (26, 30), (28, 32)  # overlapping
    ]
    f = Function(pairs=pairs)
    intervals = [(1, 5), (4, 8), (7, 10), (9, 12), (13, 15),
                 (16, 18), (20, 22), (23, 25), (26, 30), (28, 32)]
    merged = f._merge_intervals(sorted(intervals))
    assert merged == [(1, 12), (13, 15), (16, 18),
                      (20, 22), (23, 25), (26, 32)]


def test_merge_adjacent():
    pairs = [(1, 3), (3, 5), (5, 7), (8, 10)]
    f = Function(pairs=pairs)
    intervals = [(1, 3), (3, 5), (5, 7), (8, 10)]
    merged = f._merge_intervals(sorted(intervals))
    assert merged == [(1, 7), (8, 10)]


def test_merge_empty_and_single():
    f = Function(pairs=[])
    assert f._merge_intervals([]) == []
    single = [(2, 4)]
    # Only one interval, nothing to merge
    assert f._merge_intervals(single) == [(2, 4)]


def test_merge_same_start_end():

    f = Function(pairs=[(1, 3), (3, 5), (5, 7)])
    sorted_intervals = sorted(f.pairs)
    assert sorted_intervals == [(1, 3), (3, 5), (5, 7)]
    assert f._merge_intervals(sorted_intervals) == [(1, 7)]


def test_invalid_function_instantiation():
    # Not a function: duplicate x with different y
    with pytest.raises(ValueError):
        Function(pairs=[(1, 2), (1, 3)])
