from export_result import *
from generate_candidates import *
from generate_rules import *
from itertools import repeat
from load_database import *
from prune_itemsets import *
from timeit import default_timer

def apriori():
    """Performs the Apriori algorithm."""
 
    # Load database and read in the support and confidence measures.
    fname, attributes, transactions = read_database()
    min_sup = read_measure("support")
    min_conf = read_measure("confidence")

    # Start timer to keep track of processing time.
    start_time = default_timer()
    
    itemset_sups = {}

    # Generate candidate 1-itemset and prune to get the frequent 1-itemset.
    candidate_one_itemset = generate_candidate_one_itemset(transactions)
    freq_one_itemset, itemset_sups = prune_itemsets(candidate_one_itemset, transactions, min_sup, itemset_sups)

    total_freq_itemsets = set()
    freq_k_itemsets = freq_one_itemset

    # Generate k-itemsets from frequent (k-1)-itemset and then prune to get the frequent k-itemset.
    for _ in repeat(None, len(attributes)):
        candidate_itemset = generate_candidate_itemsets(freq_k_itemsets, itemset_sups)
        freq_k_itemsets, itemset_sups = prune_itemsets(candidate_itemset, transactions, min_sup, itemset_sups)
        total_freq_itemsets |= (freq_k_itemsets)

    # Generate association rules.
    candidate_rules, rule_confs = generate_rules(total_freq_itemsets, itemset_sups, min_conf)

    # End timer to get processing time.
    processing_time = default_timer() - start_time

    # Output resulting association rules to Rules file.
    num_trans = len(transactions)
    export_result(fname, num_trans, candidate_rules, min_sup, min_conf, itemset_sups, rule_confs, processing_time)

if __name__ == "__main__":
    apriori()
