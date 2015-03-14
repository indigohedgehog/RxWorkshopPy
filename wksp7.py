"""Rx Workshop: Event Processing.
Part 3 - Grouping by sliding window.
Usage:
    python wksp7.py
"""
from __future__ import print_function
import rx


class Program:

    @staticmethod
    def main():
        src = rx.Observable.from_iterable(get_input(),
                                          rx.concurrency.Scheduler.new_thread)
        res = src.window_with_count(3, 1).to_blocking()
        res.for_each(lambda w, j:
                     (print("New window " + str(j) + " created")
                      or w.subscribe(lambda x:
                                     print(" " + str(x) + " in " + str(j)))))


def get_input():
    while True:
        yield raw_input()


if __name__ == '__main__':
    Program.main()
