"""Module for loading databases."""

from __future__ import print_function

def read_database():
    """Reads in a user-specified database."""
    fname = ""
    attributes = []
    transactions = []
    while True:
        fname = raw_input("\nEnter data file name: ")
        try:
            with open(fname) as f:
                try:
                    attributes = f.readline().split()
                    if not len(attributes):
                        print("\nERROR: Data file has 0 attributes on the first line. Try another file.")
                        continue
                    # Build a list of itemsets from the transactions.
                    transactions = [{(attributes[i], value) for i, value in enumerate(line.split())} 
                                    for line in f.readlines() if len(line.split())]
                    break
                finally:
                    f.close()
        except IOError:
            print("\nERROR: No such data file. Try another file.")
        except IndexError:
            print("\nERROR: Data file contains row(s) where the number of values exceeds the number of attributes."
                  " Try another file.")
    return fname, attributes, transactions

def read_measure(measure):
    """Reads in a user-specified measure."""
    while True:
        try: 
             measure_val = float(raw_input("\nEnter minimum " + measure + " value [0.0-1.0]: "))
             if 0 <= measure_val <= 1:
                 break
             else:
                 print("\nERROR: Minimum " + measure + " value out of range. Try another value.")
        except ValueError:
            print("\nERROR: Invalid minimum " + measure + " value. Try another value.")
    return measure_val  
