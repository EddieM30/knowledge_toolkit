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
