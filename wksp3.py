"""Rx Workshop: Observables versus Events.
Part 2 - Dispose Example.
Usage:
    python wksp3.py
"""
from __future__ import print_function
import rx


class Program:
    """Main Class.
    """
    @staticmethod
    def main():
        """Main Method.
        """    
        subject = rx.subjects.Subject()
        subscription = subject.subscribe(lambda x: print(x))
        subject.on_next(42)
        subscription.dispose()
        subject.on_next(43)

if __name__ == '__main__':
    Program.main()
