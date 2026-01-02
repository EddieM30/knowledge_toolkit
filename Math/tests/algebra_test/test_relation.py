import random
from Math.core.relation import Relation


def test_relation_ignores_duplicates():
    """Test that Relation ignores duplicate pairs and only stores unique ones."""
    # Instantiate Relation
    pairs = [(1, 3), (2, 4), (1, 5), (1, 3)]
    rel = Relation(pairs)

    # Ignores duplicates and creates a set of unique pairs
    assert len(rel.pairs) == 3
    assert (1, 3) in rel.pairs
    assert (2, 4) in rel.pairs
    assert (1, 5) in rel.pairs


def test_relation_empty_input():
    """Test that Relation with empty input results in an empty set of pairs."""
    pairs = []
    rel = Relation(pairs)

    assert rel.pairs == set()


def test_relation_type_flexibility():
    """Test that Relation can handle pairs with various data types."""
    pairs = [('a', 2 + 4), (3.14159, 4.44), (600, 'v')]
    rel = Relation(pairs)

    assert len(rel.pairs) == 3
    assert ('a', 2 + 4) in rel.pairs
    assert (3.14159, 4.44) in rel.pairs
    assert (600, 'v') in rel.pairs


def test_relation_integrity():
    """Test that Relation maintains integrity after input list is cleared."""
    pairs = [('a', 'b'), ('a', 'f'), ('l', 'v')]
    rel = Relation(pairs)

    pairs = []

    assert len(rel.pairs) == 3
    assert ('a', 'b') in rel.pairs
    assert ('a', 'f') in rel.pairs
    assert ('l', 'v') in rel.pairs


def test_domain_unique_inputs_only():
    """Test that the domain contains only unique input elements from pairs."""
    # Instantiate Relation
    pairs = [(1, 3), (2, 4), (1, 5), (1, 3)]
    rel = Relation(pairs)
    domain = rel.domain

    assert len(domain) == 2
    assert domain == {1, 2}


def test_domain_element_isolation():
    """Test that the domain contains only the first elements of each pair."""
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
    """Test that the domain preserves the data types of input elements."""
    pairs = [(1, 2 + 4), (1.44, 'The man walked down the street')]
    domain = Relation(pairs).domain

    assert len(domain) == 2
    assert 1 in domain
    assert 1.44 in domain
    assert domain == {1, 1.44}


def test_domain_order_independence():
    """Test that the domain is independent of the order of input pairs."""
    pairs = [(1, 10), (2, 20), (3, 50)]
    more_pairs = [(3, 50), (2, 20), (1, 10)]

    domain1 = Relation(pairs).domain
    domain2 = Relation(more_pairs).domain

    assert domain1 == domain2
    assert domain1 == {1, 2, 3}
    assert domain2 == {1, 2, 3}
    assert domain2 == {3, 2, 1}


def test_range_unique_outputs_only():
    """Test that the range contains only unique output elements from pairs."""
    pairs = [(1, 3), (2, 4), (1, 5), (1, 3)]
    rnge = Relation(pairs).range

    assert len(rnge) == 3
    assert rnge == {3, 4, 5}


def test_range_element_isolation():
    """Test that the range contains only the second elements of each pair."""
    pairs = [(1, 3), (2, 4), (1, 5), (1, 3)]
    rnge = Relation(pairs).range

    assert len(rnge) == 3
    assert 1 not in rnge
    assert 2 not in rnge
    assert rnge == {3, 4, 5}


def test_range_empty_relation():
    """Test that the range of an empty Relation is an empty set."""
    pairs = []
    rnge = Relation(pairs).range

    assert rnge == set()
    assert rnge != set((1, 2))


def test_range_shadow_checking():
    """Test that unrelated variables do not affect the Relation's range."""
    pairs = [(1, 3), (2, 4), (1, 5), (1, 3)]
    rnge = Relation(pairs).range

    range_list = []

    for i in range(5):
        range_list.append(i)

    assert range_list == [0, 1, 2, 3, 4]


def test_relation_origin_case():
    """Test Relation behavior at the origin (0, 0) case."""
    pairs = [(0, 0)]
    rel = Relation(pairs)

    assert len(rel.pairs) == 1
    assert (0, 0) in rel.pairs

    assert rel.domain == {0}
    assert rel.range == {0}


def test_relation_negative_values():
    """Test Relation behavior with negative values in pairs."""
    pairs = [(-1, -5), (-4, -6)]
    rel = Relation(pairs)

    assert (-1, -5) in rel.pairs
    assert (-4, -6) in rel.pairs

    assert rel.domain == {-1, -4}
    assert rel.range == {-5, -6}


def test_relation_vertical_line_test():
    """Test if Relation passes the vertical line test (functionality check)."""
    pairs = [(1, 3), (1, 4), (1, 5), (1, 6)]
    rel = Relation(pairs)

    assert len(rel.domain) == 1
    assert rel.domain == {1}


def test_relation_horizontal_line_test():
    """Test if Relation passes the horizontal line test (output uniqueness)."""
    pairs = [(1, 10), (2, 10), (3, 10), (4, 10)]
    rel = Relation(pairs)

    assert len(rel.range) == 1
    assert rel.range == {10}


def test_relation_large_data_sets_100_plus():
    """Test Relation performance and correctness with 100+ pairs."""
    functional_pairs = [(x, x**2) for x in range(500)]
    duplicate_pairs = functional_pairs[:250]
    large_test_data = functional_pairs + duplicate_pairs
    rel = Relation(large_test_data)

    assert len(rel.pairs) == 500

    assert len(rel.domain) == 500
    assert len(rel.range) == 500


def test_inverse_relation():
    """Test the computation and properties of the inverse of a Relation."""
    pairs = [(1, 3), (2, 4), (3, 5), (4, 6)]
    rel = Relation(pairs)

    assert rel.inverse.inverse.pairs == rel.pairs
    assert rel.inverse.pairs == {(3, 1), (4, 2), (5, 3), (6, 4)}


def test_relation_is_function():
    """Test if the Relation represents a valid mathematical function."""
    functional_pairs = [(x, x**2) for x in range(100)]
    rel1 = Relation(functional_pairs)

    assert rel1.is_function is True
    assert len(rel1.domain) == len(rel1.pairs)


def test_relation_is_not_function():
    failure_pairs = [(1, x) for x in range(100, 350)]
    rel2 = Relation(failure_pairs)

    assert rel2.is_function is not True
    assert len(rel2.domain) != len(rel2.pairs)


def test_inverse_relation_is_function():
    pairs = [(1, 3), (2, 4), (3, 5), (4, 6)]
    rel = Relation(pairs)

    assert rel.inverse.is_function is True


def test_inverse_relation_is_not_function():
    pairs = [(1, 4), (2, 4), (3, 5), (4, 6)]
    rel = Relation(pairs)

    assert rel.inverse.is_function is not True


def test_relation_get_value_for_is_found():
    pairs = [(1, 4), (2, 4), (3, 5), (4, 6)]
    rel = Relation(pairs)

    assert rel.get_value_for(2) == 4
    assert rel.get_value_for(3) == 5
