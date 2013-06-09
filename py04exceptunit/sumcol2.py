#!/usr/bin/env python

# INSTRUCTIONS:
#
# There are 3 data files named table1.dat, table2.dat, table3.dat.
# This script calculates sum of the second column in the file.
# Run it in the command shell as
# 
#   python sumcol2.py table1.dat
#   python sumcol2.py table2.dat
#   python sumcol2.py table3.dat
#   python sumcol2.py nofile
# 
# The script crashes, because table2.dat and table3.dat are badly formatted
# and file "nofile" does not exist.
#
# Fix the marked code below so the program prints why it failed.
# For example when running with non-existing file it should give
# 
#   > python sumcol2.py nofile
#   Cannot read file nofile"
# ----------------------------------------------------------------------------

"Program for summing second column in a text data file."


def main():
    import sys
    if len(sys.argv) < 2:
        print "usage: sumcol2.py FILENAME"
        sys.exit()
    filename = sys.argv[1]
    try:
        total = sumSecondColumn(filename)
        print "the second column total for", filename, "is", total
# FIX BELOW ------------------------------------------------------------------
# (lines betwen tripple quotes are inactive)
        '''
        print "Cannot read file", filename
        print "Invalid data, 2-nd column missing in", filename
        print "Invalid data, bad number in the 2-nd column of", filename
        '''
# TO HERE --------------------------------------------------------------------
    except:
        raise
    return


def sumSecondColumn(filename):
    fp = open(filename)
    total = 0
    for line in fp:
        words = line.split()
        total += float(words[1])
    return total


if __name__ == '__main__':
    main()
