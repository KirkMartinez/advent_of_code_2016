#
# Advent of Code Day 4: Security Through Obscurity
#
from framework import *

from collections import defaultdict
from operator import itemgetter
from string import maketrans

PART1_TEST_DATA = '''aaaaa-bbb-z-y-x-123[abxyz]
a-b-c-d-e-f-g-h-987[abcde]
not-a-real-room-404[oarel]
totally-real-room-200[decoy]'''

PART2_TEST_DATA = 'qzmt-zixmtkozy-ivhz-343[zimth]'

class Day(Solver):
    def solve(self):
        lines = self.data.splitlines()
        valid_rooms = []
        sector_sum = 0
        for line in lines:
            parts = line.split('-')
            words = parts[:-1]
            sector_id, checksum = parts[-1].split('[')
            checksum = checksum[:-1]

            letters = str(''.join(words))

            #print words
            
            freq = defaultdict(int)
            for let in letters:
                freq[let] += 1

            by_freq = defaultdict(str)
            for k,v in freq.iteritems():
                by_freq[v] += k

            #print by_freq

            top_5_freq = sorted(by_freq.keys())[-5:]
            top_5_letters = []
            for freq in reversed(top_5_freq):
                alphabetical = ''.join(sorted(by_freq[freq]))
                #print "A: {0}".format(alphabetical)
                remaining = 5 - len(top_5_letters)
                if len(alphabetical) <= remaining:
                    top_5_letters += alphabetical
                elif len(alphabetical) > remaining:
                    top_5_letters += alphabetical[:remaining]

            if set(top_5_letters) == set(checksum):
                #print "Valid"
                sector_sum += int(sector_id)
                valid_rooms.append( (words, int(sector_id)) )
            else:
                #print "Not valid"
                pass

            #print top_5_freq
            #print top_5_letters
            #print

        if self.part == 1:
            self.show_result("Sector sum is: {0}".format(sector_sum))
        else:
            result = "Find the sector ID of 'where North Pole objects are stored':"
            for (name, sector_id) in valid_rooms:
                result += '\n' + self.rot(name, sector_id) + ' ' + str(sector_id)
            self.show_result(result)
            
    def rot(self, words, n):
        n = n % 26
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        rotN = maketrans(alphabet, alphabet[n:]+alphabet[:n])
        return '-'.join([str(w).translate(rotN) for w in words])

Day(4, 1, TEST, PART1_TEST_DATA).solve()
Day(4, 1, REAL).solve()
Day(4, 2, TEST, PART2_TEST_DATA).solve()
Day(4, 2, REAL).solve()

