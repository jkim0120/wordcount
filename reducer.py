#!/usr/bin/env python

from itertools import groupby
from operator import itemgetter
import sys

def read_from_mapper(file):
    for line in file:
        yield line.rstrip().split('\t', 1)

def main():
    data = read_from_mapper(sys.stdin)

    for current_word, group in groupby(data, itemgetter(0)):
        try:
            total_count = sum(int(count) for current_word, count in group)
            print '%s\t%s' % (current_word, total_count)
        except ValueError:
            pass

if __name__ == "__main__":
    main()
