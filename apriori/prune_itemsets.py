"""Module for pruning itemsets."""

from __future__ import division
from itertools import combinations

def no_infrequent_subsets(candidate_itemset, itemset_sups):
    """Checks that there are no k-1 infrequent subsets for a candidate k-itemset."""
    for subset in combinations(candidate_itemset, len(candidate_itemset) - 1):
       if frozenset(subset) not in itemset_sups:
           return False
    return True

def prune_itemsets(candidate_itemsets, transactions, min_sup, itemset_sups):
    """Prunes candidate k-itemsets of itemsets with infrequent subsets or insufficient support."""
    pruned_itemsets = set()
    for candidate_itemset in candidate_itemsets:
        # More efficient to prune a candidate k-itemset by finding a k-1 infrequent subset than to scan the database.
        if len(candidate_itemset) == 1 or no_infrequent_subsets(candidate_itemset, itemset_sups): 
            support = sum(candidate_itemset.issubset(transaction) for transaction in transactions) / len(transactions)
            if support >= min_sup:
                pruned_itemsets.add(candidate_itemset)
                itemset_sups[candidate_itemset] = support
    return pruned_itemsets, itemset_sups
