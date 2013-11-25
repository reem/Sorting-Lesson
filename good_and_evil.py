"""
Jonathan Reem
November 2013
The value of a good algorithm.
"""

def good_sort(unsorted):
    "Readable quicksort."

    # Base case. If the list is one element long or empty,
    # it has to be sorted.
    if len(unsorted) < 2:
        return unsorted

    # Initialize your lists and get the pivot.
    lesser = []
    greater = []
    pivot = unsorted[0]

    # Go through and partition the unsorted list into
    # values less than the pivot and values greater than
    # the pivot.
    for i in unsorted[1:]:
        if i < pivot:
            lesser.append(i)
        elif i >= pivot: # Equal values have to go somewhere.
            greater.append(i)

    # Recursively sort each "half". This is what makes quicksort
    # a divide and conquer algorithm.
    sorted_lesser = good_sort(lesser)
    sorted_greater = good_sort(greater)

    # Return the sorted list.
    return sorted_lesser + [pivot] + sorted_greater

from itertools import chain

def evil_sort(ulst):
    "Who knows what I do?"
    return ulst if len(ulst) < 2 else list(chain(evil_sort([i for i in ulst[1:]
        if i < ulst[0]]), [ulst[0]], evil_sort([i for i in ulst[1:] if i >=
            ulst[0]])))

def fast_sort(unsorted):
    "This sort is fast AND clear!"
    if len(unsorted) < 2:
        return unsorted

    # We're going to use these values a lot, so we store their
    # values and only call them once.
    minimum = min(unsorted)
    maximum = max(unsorted)

    # Make a list of zeroes.
    counts = []
    for _ in xrange(maximum - minimum + 1):
        counts.append(0)

    # Count the number of each value in the list
    for num in unsorted:
        counts[num-minimum] += 1

    # Recreate the list by going through the counts in order
    # and adding the amount we counted in the earlier pass.
    sorted_list = []
    for num in xrange(minimum, maximum+1):
        sorted_list += counts[num-minimum] * [num]
    return sorted_list

import numpy as np

def very_fast_sort(unsorted):
    "I am very fast, but very difficult to understand."
    unsorted = np.asarray(unsorted)
    return (np.repeat(np.arange(1+unsorted.max()),
        np.bincount(unsorted))).tolist()

def radix_sort(unsorted):
    "Radix sort for ints under 2**16"
    def two_bytes(num):
        "Gets the first two bytes of an integer."
        return ((num & 0xff00) >> 8, (num & 0xff))
    def bytes_to_int(byte1, byte2):
        "Gets an integer from its bytes."
        return (((0 << 8) + byte1) << 8) + byte2

    buckets = [[] for _ in xrange(256)]

    for num in unsorted:
        num_bytes = two_bytes(num)
        buckets[num_bytes[0]].append(num_bytes[1])

    buckets = [fast_sort(bucket) for bucket in buckets]

    return [bytes_to_int(bucket_ind, i) for bucket_ind, bucket in
            enumerate(buckets) for i in bucket]

import sys
from sort_test import sort_test

def main():
    "Tests the sort."
    try:
        size = int(sys.argv[1])
    except IndexError:
        size = 6
    sort_test([evil_sort,
               good_sort,
               fast_sort,
               very_fast_sort,
               radix_sort,
               sorted], max_size_order=size)

if __name__ == '__main__':
    main()
