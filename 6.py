#
# Advent of Code Day 6: Signals and Noise
#
from framework import *

from collections import defaultdict
from operator import itemgetter

# Put test input data here:
TEST_DATA = '''eedadn
drvtee
eandsr
raavrd
atevrs
tsrnev
sdttsa
rasrtv
nssdts
ntnada
svetve
tesnvt
vntsnd
vrdear
dvrsen
enarar'''

class Day(Solver):
    def solve(self):
        # initialize data structures
        lines = self.data.splitlines()
        freqs = defaultdict() # dict mapping position to dict mapping letters to their frequency 
        chars = len(lines[0])
        for i in range(chars):
            freqs[i] = defaultdict(int)

        # collect the frequency of each letter at each position
        for line in lines: 
            for (i,ch) in enumerate(line):
                freqs[i][ch] += 1

        result = []
        for i in range(chars):
            if self.part == 1:
                most_freq = sorted(freqs[i].items(), key = itemgetter(1), reverse=True)
            else:
                most_freq = sorted(freqs[i].items(), key = itemgetter(1))

            result.append(most_freq[0][0])

        self.show_result(''.join(result))

Day(6, 1, TEST, TEST_DATA).solve()
Day(6, 1, REAL).solve()
Day(6, 2, TEST, TEST_DATA).solve()
Day(6, 2, REAL).solve()

