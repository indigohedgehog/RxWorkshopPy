"""Rx Workshop: Event Processing.
Part 1 - Blocking Foreach.
Usage:
    python wksp4.py
"""
from __future__ import print_function
import rx


class Program:
    """Main class.
    """
    @staticmethod
    def main():
        """Main method.
        """
        src = rx.Observable.from_iterable(getInput(),
                                          rx.concurrency.Scheduler.new_thread)
        xs = src.to_blocking()
        for x in xs:
            print(x)


def getInput():
    """Stream generator.
    """
    while True:
        yield raw_input()

if __name__ == '__main__':
    Program.main()
