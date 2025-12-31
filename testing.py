from src.algebra.functions import Function
from src.algebra.relation import Relation


pairs = [(1, 4), (2, 4), (3, 5), (4, 6)]
rel = Relation(pairs)
f = Function(relation=rel, rule=lambda x: 2 * (x + 3 * 3 * 3))

g = f.shift_vertical(5)
print(g(2))
