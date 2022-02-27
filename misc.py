"""a module storing auxiliary functions for easy development"""

import colorama
from colorama import Fore as F

colorama.init()


def output(passed, result, note):
    """auxiliary function for color output of the result"""
    if passed:
        print(f"{F.GREEN}{note}passed")
    else:
        print(f"{F.RED}{note}failed ({result})")
    print(F.RESET, end='')
