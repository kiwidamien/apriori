import pytest

@pytest.fixture
def dataset():
    return [[1, 3, 4], [2, 3, 5], [1, 2, 3, 5], [2, 5]]


# def test_single_set_contains_1_through_5(dataset):
#     single_item_sets = apriori.create_single_item_sets(dataset)
#     should_be_in_set = [frozenset({num}) for num in range(1, 6)]
#     for itemset in should_be_in_set:
#         assert itemset in single_item_sets, f'Expected {itemset} to be in {single_item_sets}, and it was not'
#
#
# def test_empty_set_has_no_single_items_sets():
#     single_item_sets = apriori.create_single_item_sets([[]])
#     assert len(single_item_sets) == 0, f'Expected no data to produce empty set, instead producted {single_item_sets}'
#
#
# def test_support_in_dataset(dataset):
#     # Find the fractions by hand
#     answers = {
#         frozenset({1}): 0.5,  # item 1 in half the transactions
#         frozenset({2}): 0.75, # item 2 in 3 of 4 transactions
#         frozenset({3}): 0.75, # item 3 in 3 of 4 transactions
#         frozenset({4}): 0.25,
#         frozenset({5}): 0.75,
#         frozenset({1, 3}): 0.5, # items 1 & 3 are in half transactions
#         frozenset({2, 5}): 0.75,
#         frozenset({3, 5}): 0.5,
#         frozenset({2, 3}): 0.5,
#         frozenset({1, 5}): 0.25,
#         frozenset({1, 2}): 0.25,
#         frozenset({2, 3, 5}): 0.5
#     }
#     _, supportData = apriori.apriori(dataset, minSupport=0.5)
#     assert answers == supportData, 'Did not match expected result'
#
#
# def test_items_that_have_min_support(dataset):
#     single_item_set = apriori.create_single_item_sets(dataset)
#     support_single_items = {
#         frozenset({1}): 0.5,  # item 1 in half the transactions
#         frozenset({2}): 0.75,  # item 2 in 3 of 4 transactions
#         frozenset({3}): 0.75,  # item 3 in 3 of 4 transactions
#         frozenset({4}): 0.25,
#         frozenset({5}): 0.75,
#     }
#
#     min_support_zero = set(single_item_set)
#     enough_support, _ = apriori.scan_dataset(dataset, single_item_set, minSupport=0.0)
#     assert min_support_zero==set(enough_support), 'Did not get back all items'
#
#     at_least_half_support = set([element for element, support in support_single_items.items() if support>=0.5])
#     enough_support, _ = apriori.scan_dataset(dataset, single_item_set, minSupport=0.5)
#     assert at_least_half_support==set(enough_support), f'Did not identify items with 0.5 support or more'
#
#     at_least_half_support = set([element for element, support in support_single_items.items() if support >= 0.75])
#     enough_support, _ = apriori.scan_dataset(dataset, single_item_set, minSupport=0.75)
#     assert at_least_half_support==set(enough_support), f'Did not identify items with 0.75 support or more'
#
#
# @pytest.mark.parametrize('elements,k,expected',[
#                      ([1, 2, 5], 2, [{1,2}, {1,5}, {2, 5}]),
#                      ])
# def test_apriori_generation(elements, k, expected):
#     freeze = [frozenset({element}) for element in elements]
#     sorted_generate = sorted(apriori.apriori_generate(freeze, k))
#     assert sorted_generate==expected
#
