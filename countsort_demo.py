"""
Jonathan Reem
Nice Demonstration of countsort
"""

from sys import stdout, argv
from time import sleep
from random import shuffle, randint


def countsort_demo(unsorted, sleep_time):
    "Demonstrates countsort with fancy printing."
    minimum = min(unsorted)
    maximum = max(unsorted)

    counts = [0] * (maximum - minimum + 1)

    for num_ind, num in enumerate(unsorted):
        counts_index = num - minimum
        counts[counts_index] += 1

        printable_counts = [counts[i] if i != counts_index
                            else "*{}*".format(counts[i])
                            for i in range(len(counts))]
        printable_unsorted = [unsorted[i] if i != num_ind
                              else "*{}*".format(unsorted[i])
                              for i in range(len(unsorted))]

        stdout.write("\rUnsorted: {} | Counts: {}".format(printable_unsorted,
                                                          printable_counts))
        stdout.flush()
        sleep(sleep_time)

    stdout.write("\rUnsorted: {} | Counts: {}             ".format(unsorted,
                                                                   counts))
    stdout.write("\n")
    stdout.flush()

    sorted_list = []
    for num, count in enumerate(counts):
        section = [num + minimum] * count

        stdout.write("\rSorted: {} | Next: {}".format(sorted_list, section))
        stdout.flush()
        sleep(sleep_time)

        sorted_list.extend(section)

    stdout.write("\rSorted: {}                       \n".format(sorted_list))
    stdout.flush()

    return sorted_list


def main():
    "Runs countsort demo."
    try:
        sleep_time = float(argv[1].strip())
    except IndexError:
        sleep_time = 2

    rlist = [randint(0, 4) for _ in range(10)]
    if 0 not in rlist:
        rlist.pop()
        rlist.append(0)

    shuffle(rlist)
    countsort_demo(rlist, sleep_time)


if __name__ == '__main__':
    main()
