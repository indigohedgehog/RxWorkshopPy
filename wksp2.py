"""Rx Workshop: Observables versus Events.
Part 1 - Little Example.
Usage:
    python wksp2.py
"""
from __future__ import print_function
import rx

class Program:
    """Main Class.
    """
    S = rx.subjects.Subject()

    @staticmethod
    def main():
        """Main Method.
        """
        p = Program()
        p.S.subscribe(lambda x: print(x))
        p.S.on_next(1)
        p.S.on_next(2)
        p.S.on_next(3)        

if __name__ == '__main__':
    p = Program()
    p.main()
