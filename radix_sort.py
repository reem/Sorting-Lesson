"""
Jonathan Reem
Radix Sort
"""

import itertools

def radix_sort(unsorted):
    "Fast implementation of radix sort for any size num."
    maximum, minimum = max(unsorted), min(unsorted)

    max_bits = maximum.bit_length()
    highest_byte = max_bits // 8 if max_bits % 8 == 0 else (max_bits // 8) + 1

    min_bits = minimum.bit_length()
    lowest_byte = min_bits // 8 if min_bits % 8 == 0 else (min_bits // 8) + 1

    sorted_list = unsorted
    for offset in xrange(lowest_byte, highest_byte):
        sorted_list = radix_sort_offset(sorted_list, offset)

    return sorted_list

def radix_sort_offset(unsorted, offset):
    "Helper function for radix sort, sorts each offset."
    byte_check = (0xFF << offset*8)

    buckets = [[] for _ in xrange(256)]

    for num in unsorted:
        byte_at_offset = (num & byte_check) >> offset*8
        buckets[byte_at_offset].append(num)

    return itertools.chain.from_iterable(buckets)

import sys
from sort_test import sort_test

def main():
    "Tests the sort."
    try:
        size = int(sys.argv[1].strip())
    except IndexError:
        size = 6
    sort_test([radix_sort, sorted], max_size_order=size)

if __name__ == '__main__':
    main()
