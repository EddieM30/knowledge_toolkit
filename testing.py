from Math.core.functions import Function
from Math.core.relation import Relation

rel = Relation([(x, x**2) for x in range(-5, 6)])
f = Function(pairs=[
    (1, 5),
    (4, 8),
    (7, 10),
    (9, 12),
    (13, 15),
    (16, 18),
    (20, 22),
    (23, 25),
    (26, 30),
    (28, 32),
])

print(f.intervals_of_increase())
print(f._merge_intervals(f.intervals_of_increase()))
