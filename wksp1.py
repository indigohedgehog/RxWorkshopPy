"""Rx Workshop: Introduction.
Usage:

    python wks1.py
"""
from __future__ import print_function
import rx

class Program:
    """Wrapped in class as in the example.
    """
    
    @staticmethod
    def main():
        """Main method.
        """
        xs = rx.Observable.from_("Hello World")
        xs.subscribe(lambda x: print(x))
        raw_input()

if __name__ == '__main__':
    Program.main()
