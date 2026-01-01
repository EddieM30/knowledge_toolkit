from Math.core.functions import Function
from Math.core.relation import Relation


f_even = Function(relation=Relation([(x, x**2)
                                     for x in range(-5, 6)]), rule=lambda x: x**2)

f_odd = Function(relation=Relation([(x, x**3)
                                    for x in range(-5, 6)]), rule=lambda x: x**3)

f_even.check_symmetry()
f_odd.check_symmetry()
