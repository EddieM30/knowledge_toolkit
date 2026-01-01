
from Math.core.functions import Function
from Math.core.relation import Relation

functional_rel = Relation([(x, x**2) for x in range(10)])
non_function_rel = Relation([(1, 2), (2, 3), (1, 5)])


def test_is_function_on_instantiation():

    func = Function(functional_rel)
    assert func.is_function is True


def test_is_not_function_on_instantiation():
    func = Function(non_function_rel)
    assert func.is_function is False


def test_rule_evaluation():
    f = Function(relation=functional_rel, rule=lambda x: x**2)

    assert f(4) == 16
    assert f(5) == 25


def test_compose():
    f = Function(relation=Relation([(x, x**2)
                 for x in range(-5, 6)]), rule=lambda x: x**2)
    g = Function(relation=Relation([(x, x + 1)
                 for x in range(-5, 6)]), rule=lambda x: x + 1)

    h = f.compose(g)

    assert h(2) == 9  # (2+1)^2 = 9
    assert h(0) == 1  # (0+1)^2 = 1
    assert h(-2) == 1  # (-2+1) = 1


def test_compose_with_self():
    f = Function(relation=Relation([(x, x - 3)
                 for x in range(-5, 6)]), rule=lambda x: x - 3)

    h = f.compose(f)

    assert h(2) == -4
    assert h(-7) == -13
    assert h(5) == -1


def test_compose_identity():
    i = Function.identity(-5, 6)
    f = Function(relation=Relation([(x, x**2)
                 for x in range(-5, 6)]), rule=lambda x: x**2)
    h = f.compose(i)  # h = f(i(x))

    assert i(2) == 2
    assert h(2) == 4
    assert h(100) == 10000
    assert h(2 * (3 - 5)) == (2 * (3 - 5))**2
    assert h(2 * (3 - 5)) == 16


def test_compose_constant():
    f = Function.constant(7)

    g = Function(relation=Relation([(x, x**3)
                 for x in range(-5, 6)]), rule=lambda x: x**3)
    h = f.compose(g)

    assert f(1) == 7
    assert h(9) == 7


def test_vertical_shift():
    pass
