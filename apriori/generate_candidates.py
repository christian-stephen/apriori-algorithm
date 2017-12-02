"""Module for generating candidate k-itemsets."""

from itertools import combinations

def generate_candidate_one_itemset(transactions):
    """Generates candidate 1-itemset."""
    return {frozenset([item, item]) for item in set.union(*transactions)}

def generate_candidate_itemsets(itemsets):
    """Generates candidate k-itemsets."""
    candidate_itemsets = set()
    for itemset1, itemset2 in combinations(itemsets, 2):
        # Find the symmetric difference to ensure only the first k-2 items match.
        itemlist_diff = list(itemset1 ^ itemset2)
        if len(itemlist_diff) == 2 and itemlist_diff[0][0] != itemlist_diff[1][0]:
            candidate_itemsets.add(itemset1 | itemset2)
    return candidate_itemsets
