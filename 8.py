#
# Advent of Code Day 8
#
from framework import *

#from collections import defaultdict
#from operator import itemgetter
#import re

from logging import basicConfig, debug, info, DEBUG, ERROR
basicConfig(level=ERROR)

# Put test input data here:
PART1_TEST_DATA = '''
'''

PART2_TEST_DATA = '''
'''

class Day(Solver):
    def solve(self):
        self.show_result(tls)

Day(8, 1, TEST, PART1_TEST_DATA).solve()
Day(8, 1, REAL).solve()
Day(8, 2, TEST, PART2_TEST_DATA).solve()
Day(8, 2, REAL).solve()

