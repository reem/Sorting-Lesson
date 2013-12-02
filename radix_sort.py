"""
Jonathan Reem
November 2013
Radix Sort
"""

import itertools
import sys
from sort_test import sort_test


def radix_sort(unsorted, radix=12):
    "Fast implementation of radix sort for any size num."
    maximum, minimum = max(unsorted), min(unsorted)

    max_bits = maximum.bit_length()
    highest_byte = max_bits // radix if not (max_bits % radix) \
        else (max_bits // radix) + 1

    min_bits = minimum.bit_length()
    lowest_byte = min_bits // radix if not (min_bits % radix) \
        else (min_bits // radix) + 1

    sorted_list = unsorted
    for offset in xrange(lowest_byte, highest_byte):
        sorted_list = radix_sort_offset(sorted_list, offset, radix)

    return sorted_list


def radix_sort_offset(unsorted, offset, radix):
    "Helper function for radix sort, sorts each offset."
    buckets = [[] for _ in xrange(1 << radix)]

    byte_check = (1 << radix) - 1
    byte_access = offset * radix

    # bucketappender optimization due to Tim Peters :)
    bucketappender = [bucket.append for bucket in buckets]
    for num in unsorted:
        bucketappender[(num >> byte_access) & byte_check](num)

    return itertools.chain.from_iterable(buckets)


def main():
    "Tests the sort."
    try:
        size = int(sys.argv[1].strip())
    except IndexError:
        size = 6
    sort_test([radix_sort, sorted], max_size_order=size)

if __name__ == '__main__':
    main()
