import requests
import sys

from my_cookies import cookies

r = requests.get('http://adventofcode.com/2016/day/3/input', cookies=cookies)
if r.status_code != 200:
    print "Can't get input: {0}".format(r.status_code)
    print r.headers
    sys.exit(1)

data = r.text

def check(a, b, c):
    a = int(a)
    b = int(b)
    c = int(c)
    if (a+b>c) and (b+c>a) and (c+a>b):
        return 1
    else:
        return 0

def part1():
    ok = 0
    for line in data.splitlines():
        a,b,c = str(line).strip().split()
        ok += check(a,b,c)

    print ok

# part2

#data = '''1 2 3
#    4 5 6
#    7 8 9'''

lines = data.splitlines()
grid = [str(line).strip().split() for line in lines]

ok = 0
offset=0
while (offset+2)<len(lines):
    for col in range(3):
        print grid[offset][col], grid[offset+1][col], grid[offset+2][col]
        ok += check(grid[offset][col], grid[offset+1][col], grid[offset+2][col])
    offset += 3

print ok

