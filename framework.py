#
# Advent of Code Solver base class
#
import requests
import sys

from aoc_cookies import cookies

# Data set types
TEST = 0
REAL = 1

class Solver(object):
    def __init__(self, day, part=1, dataset=TEST, test_data=''):
        self.day = day
        self.part = part
        self.dataset = dataset
        if dataset == TEST:
            self.data = test_data
        else:
            self.get_real_data(day)

    def get_real_data(self, day):
        url = 'http://adventofcode.com/2016/day/{0}/input'.format(day)
        r = requests.get(url, cookies=cookies)
        if r.status_code != 200:
            print "Got {0} from {1}".format(r.status_code, url)
            print "Aborting."
            sys.exit(1)

        self.data = r.text

    def solve(self):
        print "Not yet implemented..."
    
    def show_result(self, result):
        if self.dataset == TEST:
            print "Day {0}, Part {1}, test data set: {2}".format(self.day, self.part, result)
        else:
            print "Day {0}, Part {1}, real data set: {2}".format(self.day, self.part, result)

