# Lesson on Sorting #
Steps:
 * Only test `good_sort` and `evil_sort`.
 * Ask students if `good_sort` or `evil_sort` is going to run faster.
 * Explain that shorter code != faster code then run the test
   * Lo and behold, `evil_sort` is slower.
 * Explain that although we could spend a lot of time trying to make
   `good_sort` faster through little tricks, what really matters is your
   underlying algorithm.
 * Add `sorted` to the tested algorithms and demonstrate that `good_sort`
   is never going to be faster than `sorted`. If we want to beat it, we'll
   need a better algorithm.
 * Add `fast_sort` to tested sorts. `fast_sort` is a basic-python-syntax-only
   implementation of countsort that beats `sorted` if you cheat on the range
   of the lists a bit.
 * Explain how `fast_sort` works and why it will be faster than `good_sort` and
   maybe even `sorted`. Run the test.
 * We've beaten `sorted`! Hurrah! Sometimes it pays to obfuscate your code a
   bit if you really get a performance boost and the system is
   performance-critical.
 * Add `very_fast_sort`, which is a countsort using `numpy` functions, so it's
   even faster. Run the test again and show that `very_fast_sort` is even
   faster.
 * What's the tradeoff?
   * You have to add another dependency (numpy) which doesn't work everywhere.
      For instance, it hasn't been ported to python3 or to pypy.
   * This is much harder to read, so you have to comment it really well, and
      if something doesn't work... It's very hard to debug.
   * You should only do something like this if you really absolutely need the
      performance, otherwise it's not worth the tradeoff.
 * (If we have time) Wanna see another cool sort? Explain `radix_sort` and add
   it to the tester. Turns out it isn't as fast as `fast_sort` on this data,
   but if we were going to a different kind of data, it might be *much* faster.
 * Ultimately, you should pretty much always use `sorted` unless you know that
   it's the bottle-neck in your code and you know enough about your data to
   postulate that a different algorithm like countsort or radix sort that
   cheats a little bit would be faster.
