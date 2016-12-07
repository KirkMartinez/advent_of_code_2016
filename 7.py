#
# Advent of Code Day 7: Internet Protocol Version 7
#
from framework import *

from collections import defaultdict
from operator import itemgetter
import re

from logging import basicConfig, debug, info, DEBUG, ERROR
basicConfig(level=ERROR)

# Put test input data here:
PART1_TEST_DATA = '''abba[mnop]qrst
abcd[bddb]xyyx
aaaa[qwer]tyui
ioxxoj[asdfgh]zxcvbn'''

#abba[mnop]qrst supports TLS (abba outside square brackets).
#abcd[bddb]xyyx does not support TLS (bddb is within square brackets, even though xyyx is outside square brackets).
#aaaa[qwer]tyui does not support TLS (aaaa is invalid; the interior characters must be different).
#ioxxoj[asdfgh]zxcvbn supports TLS (oxxo is outside square brackets, even though it's within a larger string).

PART2_TEST_DATA = '''aba[bab]xyz
xyx[xyx]xyx
aaa[kek]eke
zazbz[bzb]cdb'''

#aba[bab]xyz supports SSL (aba outside square brackets with corresponding bab within square brackets).
#xyx[xyx]xyx does not support SSL (xyx, but no corresponding yxy).
#aaa[kek]eke supports SSL (eke in supernet with corresponding kek in hypernet; the aaa sequence is not related, because the interior character must be different).
#zazbz[bzb]cdb supports SSL (zaz has no corresponding aza, but zbz has a corresponding bzb, even though zaz and zbz overlap).

class Day(Solver):
    def part1_solve(self):
        # initialize data structures
        lines = self.data.splitlines()
        tls = 0

        for line in lines:
            info(line)
            has_abba = False
            denies_abba = False
            in_bracket = False
            word = ''
            for ch in line:
                if ch == '[':
                    debug("Check {0}".format(word))
                    if self.has_abba(word):
                        has_abba = True
                    word = ''
                    in_bracket = True
                elif ch == ']':
                    in_bracket = False
                    debug("Check {0}".format(word))
                    if self.has_abba(word):
                        denies_abba = True
                    word = ''
                else:
                    word += ch

            debug("Check {0}".format(word))
            if self.has_abba(word):
                has_abba = True

            debug("has: {0}".format(has_abba))
            debug("not: {0}".format(denies_abba))

            if has_abba and not denies_abba:
                tls += 1

        self.show_result(tls)

    def has_abba(self, word):
        yes = False
        for i in range(len(word)-3):
            if word[i] == word[i+3] and word[i+1] == word[i+2] and word[i] != word[i+1]:
                yes = True
        return yes

    def get_abas(self, word):
        result = []
        for i in range(len(word)-2):
            if word[i] == word[i+2] and word[i] != word[i+1]:
                result.append( word[i:i+3] )
        return result

    def solve(self):
        # initialize data structures
        lines = self.data.splitlines()
        tls = 0

        for line in lines:
            info(line)
            abas = []
            babs = []
            in_bracket = False
            word = ''
            for ch in line:
                if ch == '[':
                    debug("Check {0}".format(word))
                    abas += self.get_abas(word)
                    word = ''
                    in_bracket = True
                elif ch == ']':
                    in_bracket = False
                    debug("Check {0}".format(word))
                    babs += self.get_abas(word)
                    word = ''
                else:
                    word += ch

            debug("Check {0}".format(word))
            abas += self.get_abas(word)

            # Turn babs into abas so we can compare sets
            abbabs = []
            for i in babs:
                abbabs.append( i[1]+i[0]+i[1] )

            debug("abas: {0}".format(abas))
            debug("babs: {0}".format(babs))
            debug("abbabs: {0}".format(abbabs))

            if set(abas).intersection(set(abbabs)):
                debug("yes")
                tls += 1

        self.show_result(tls)


Day(7, 1, TEST, PART1_TEST_DATA).part1_solve()
Day(7, 1, REAL).part1_solve()
Day(7, 2, TEST, PART2_TEST_DATA).solve()
Day(7, 2, REAL).solve()

