"""Module for generating candidate k-itemsets."""

def generate_candidate_one_itemset(transactions):
    """Generates candidate 1-itemset."""
    candidate_one_itemset = {frozenset([item, item]) for item in set.union(*transactions)}
    return candidate_one_itemset

def generate_candidate_itemsets(itemsets, itemset_sups):
    """Generates candidate k-itemsets."""
    candidate_itemsets = set()
    for itemset1 in itemsets:
        for itemset2 in itemsets:
            # Find the symmetric difference to ensure only the first k-2 items match.
            itemlist_diff = list(itemset1 ^ itemset2)
            if len(itemlist_diff) == 2 and itemlist_diff[0][0] != itemlist_diff[1][0]: 
                candidate_itemset = itemset1 | itemset2
                candidate_itemsets.add(candidate_itemset)
    return candidate_itemsets
