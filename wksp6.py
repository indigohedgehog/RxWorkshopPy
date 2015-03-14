"""Rx Workshop: Event Processing.
Part 3 - Grouping by window.
Usage:
    python wksp6.py
"""
from __future__ import print_function
import rx


class Program:

    @staticmethod
    def main():
        src = rx.Observable.from_iterable(get_input(),
                                          rx.concurrency.Scheduler.new_thread)
        res = src.window_with_count(3).to_blocking()
        res.for_each(lambda w: print("New window created")
                     and w.subscribe(print()))


def get_input():
    while True:
        yield raw_input()


if __name__ == '__main__':
    Program.main()
