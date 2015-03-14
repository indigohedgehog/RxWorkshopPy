"""Rx Workshop: Event Processing.
Part 2 - Grouping.
Usage:
    python wksp5.py
"""
from __future__ import print_function
import rx


class Program:
    
    @staticmethod
    def main():
        src = rx.Observable.from_iterable(get_input(),
                                          rx.concurrency.Scheduler.new_thread)
        res = src.group_by(lambda s: len(s)).to_blocking()
        res.for_each(lambda g: print("New group with length = " + str(g.key))
                     and g.subscribe(lambda x: print
                                     (" " + str(x) + " member of " + g.key)))


def get_input():
    while True:
        yield raw_input()


if __name__ == '__main__':
    Program.main()
