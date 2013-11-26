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
    counts = [0]*(maximum - minimum + 1)

    # Count the number of each value in the list
    for num in unsorted:
        counts[num-minimum] += 1

    # Recreate the list by going through the counts in order
    # and adding the amount we counted in the earlier pass.
    sorted_list = []
    for num in xrange(minimum, maximum+1):
        sorted_list += counts[num-minimum] * [num]
    return sorted_list

import sys
from sort_test import sort_test

def main():
    "Tests the sort."
    try:
        size = int(sys.argv[1].strip())
    except IndexError:
        size = 6
    sort_test([evil_sort,
               good_sort,
               fast_sort,
               sorted], max_size_order=size)

if __name__ == '__main__':
    main()
