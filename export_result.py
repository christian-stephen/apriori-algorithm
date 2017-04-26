"""Module for exporting Apriori algorithm results."""

from __future__ import print_function

def export_result(fname, num_trans, candidate_rules, minsup, minconf, itemset_sups, rule_confs, processing_time):
    """Prints association rules to Rules file."""  
    try:
        f = open('Rules', 'w')
        try:
            print("Summary:", file=f)
            print("---------------------------------------------------", file=f)
            print("Data filename: " + fname, file=f)
            print("Total rows in the original set: " + str(num_trans), file=f)
            print("Total rules discovered: " + str(len(candidate_rules)), file=f)
            print("The selected measures: Support=" + str("%.2f" % minsup) + " Confidence=" + str("%.2f" % minconf), file=f)
            print("Total processing time: %.3f" % processing_time + " seconds", file=f)
            print("---------------------------------------------------", end="", file=f)
            print("\nDiscovered Rules:\n", end="", file=f)
            for i, candidate_rule in enumerate(candidate_rules, 1):
                print("\nRule #" + str(i) + ": (Support=" + str("%.2f" % itemset_sups[candidate_rule[0] | candidate_rule[1]]) 
                    + ", Confidence=" + str("%.2f" % rule_confs[candidate_rule]) + ")\n{ ", end="", file=f)
                for antecendent in candidate_rule[0]:
                    print(antecendent[0] + "=" + antecendent[1] + " ", end="", file=f)
                print("}\n    ---> { ", end="", file=f)
                for consequence in candidate_rule[1]:
                    print(consequence[0] + "=" + consequence[1] + " ", end="", file=f)
                print("} ", file=f)
        finally:
            f.close()
    except IOError:
        print("\nERROR: Unable to create \"Rules\" file.")
    else:
        print("\nApriori algorithm finished.")
        print("Total processing time: %.3f" % processing_time + " seconds.")
        if candidate_rules:
            print("Association rules saved in the file \"Rules.\"\n") 
        else:
            print("WARNING: 0 association rules were discovered. \"Rules\" file is empty.\n")
