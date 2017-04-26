# Python Implementation of the Apriori Algorithm 

The code is a Python implementation of the Apriori algorithm for association rule mining.

## Usage

To run the program on a Unix-based system, extract the files to a directory and type the following:
```
$ Python2 apriori.py
```
When prompted, enter a data file (e.g., "sample_data") with the following format: the first line contains column headings (i.e., attribute names) and every following row contains the values that represent a tuple. Then, enter support and confidence values (i.e., values between 0 and 1). The resulting association rules are saved to the "Rules" file.

Here is a sample run:
```
Enter data file name: sample_data

Enter minimum support value [0.0-1.0]: 0.5

Enter minimum confidence value [0.0-1.0]: 0.7

Apriori algorithm finished.
Total processing time: 0.007 seconds.
Association rules saved in the file "Rules."
```

## License

The MIT License (MIT)
