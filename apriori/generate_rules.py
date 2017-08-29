"""Module for generating association rules."""

from __future__ import division
from itertools import combinations

def generate_rules(freq_itemsets, itemset_sups, min_conf):
    """Generates association rules with sufficient confidence."""
    rules = []
    rule_confs = {}

    def sufficient_confidence(candidate_rule):
        """Checks whether a candidate rule has sufficient confidence."""
        confidence = (itemset_sups[candidate_rule[0] | candidate_rule[1]] / itemset_sups[candidate_rule[0]] 
                      if itemset_sups[candidate_rule[0]] 
                      else 0)
        if confidence >= min_conf:
            rule_confs[candidate_rule] = confidence
            return True
        return False

    # Confidence-based candidate pruning.
    for freq_itemset in freq_itemsets:
        k = len(freq_itemset)
        pruned_freq_itemset = freq_itemset
        while k > 1:
            antecedents = set()
            for comb in combinations(pruned_freq_itemset, k - 1):
                antecedent = frozenset(comb)
                consequence = freq_itemset - antecedent
                candidate_rule = (antecedent, consequence)
                if sufficient_confidence(candidate_rule):
                    antecedents |= antecedent
                    rules.append(candidate_rule)
            pruned_freq_itemset = antecedents
            if k > len(pruned_freq_itemset):
                k = len(pruned_freq_itemset) 
            k -= 1
    return rules, rule_confs  
