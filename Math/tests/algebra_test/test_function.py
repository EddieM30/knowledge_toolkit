
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


def test_vertical_shift():
    pass
