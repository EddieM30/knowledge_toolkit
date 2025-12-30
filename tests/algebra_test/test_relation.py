from src.algebra.relation import Relation


def test_relation_ignores_duplicates():
    # Instantiate Relation
    pairs = [(1, 3), (2, 4), (1, 5), (1, 3)]
    rel = Relation(pairs)

    # Ignores duplicates and creates a set of unique pairs
    assert len(rel.pairs) == 3
    assert (1, 3) in rel.pairs
    assert (2, 4) in rel.pairs
    assert (1, 5) in rel.pairs


def test_relation_empty_input():
    pairs = []
    rel = Relation(pairs)

    assert rel.pairs == set()


def test_relation_type_flexibility():
    pairs = [('a', 2 + 4), (3.14159, 4.44), (600, 'v')]
    rel = Relation(pairs)

    assert len(rel.pairs) == 3
    assert ('a', 2 + 4) in rel.pairs
    assert (3.14159, 4.44) in rel.pairs
    assert (600, 'v') in rel.pairs


def test_relation_integrity():
    pairs = [('a', 'b'), ('a', 'f'), ('l', 'v')]
    rel = Relation(pairs)

    pairs = []

    assert len(rel.pairs) == 3
    assert ('a', 'b') in rel.pairs
    assert ('a', 'f') in rel.pairs
    assert ('l', 'v') in rel.pairs


def test_domain_unique_inputs_only():
    # Instantiate Relation
    pairs = [(1, 3), (2, 4), (1, 5), (1, 3)]
    rel = Relation(pairs)
    domain = rel.domain

    assert len(domain) == 2
    assert domain == {1, 2}


def test_domain_element_isolation():
    pairs = [(1, 2), (3, 4), (5, 6)]
    domain = Relation(pairs).domain

    assert len(domain) == 3
    assert 1 in domain
    assert 3 in domain
    assert 5 in domain
    assert domain == {1, 3, 5}
    assert 2 not in domain
    assert 4 not in domain
    assert 6 not in domain


def test_domain_data_type_consistency():
    pairs = [(1, 2 + 4), (1.44, 'The man walked down the street')]
    domain = Relation(pairs).domain

    assert len(domain) == 2
    assert 1 in domain
    assert 1.44 in domain
    assert domain == {1, 1.44}


def test_domain_order_independence():
    pairs = [(1, 10), (2, 20), (3, 50)]
    more_pairs = [(3, 50), (2, 20), (1, 10)]

    domain1 = Relation(pairs).domain
    domain2 = Relation(more_pairs).domain

    assert domain1 == domain2
    assert domain1 == {1, 2, 3}
    assert domain2 == {1, 2, 3}
    assert domain2 == {3, 2, 1}


def test_range_unique_outputs_only():
    pairs = [(1, 3), (2, 4), (1, 5), (1, 3)]
    rnge = Relation(pairs).range

    assert len(rnge) == 3
    assert rnge == {3, 4, 5}


def test_range_element_isolation():
    pairs = [(1, 3), (2, 4), (1, 5), (1, 3)]
    rnge = Relation(pairs).range

    assert len(rnge) == 3
    assert 1 not in rnge
    assert 2 not in rnge
    assert rnge == {3, 4, 5}


def test_range_empty_relation():
    pairs = []
    rnge = Relation(pairs).range

    assert rnge == set()
    assert rnge != set((1, 2))


def test_range_shadow_checking():
    pairs = [(1, 3), (2, 4), (1, 5), (1, 3)]
    rnge = Relation(pairs).range

    range_list = []

    for i in range(5):
        range_list.append(i)

    assert range_list == [0, 1, 2, 3, 4]


def test_relation_origin_case():
    # (0, 0)
    pass


def test_relation_negative_values():
    pass


def test_relation_vertical_line_test():
    pass


def test_relation_horizontal_line_test():
    pass


def test_relation_large_data_sets_100_plus():
    pass


def test_inverse_relation():
    pass


def test_relation_function_verification():
    pass
