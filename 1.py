import sys

i="R4, R1, L2, R1, L1, L1, R1, L5, R1, R5, L2, R3, L3, L4, R4, R4, R3, L5, L1, R5, R3, L4, R1, R5, L1, R3, L2, R3, R1, L4, L1, R1, L1, L5, R1, L2, R2, L3, L5, R1, R5, L1, R188, L3, R2, R52, R5, L3, R79, L1, R5, R186, R2, R1, L3, L5, L2, R2, R4, R5, R5, L5, L4, R5, R3, L4, R4, L4, L4, R5, L4, L3, L1, L4, R1, R2, L5, R3, L4, R3, L3, L5, R1, R1, L3, R2, R1, R2, R2, L4, R5, R1, R3, R2, L2, L2, L1, R2, L1, L3, R5, R1, R4, R5, R2, R2, R4, R4, R1, L3, R4, L2, R2, R1, R3, L5, R5, R2, R5, L1, R2, R4, L1, R5, L3, L3, R1, L4, R2, L2, R1, L1, R4, R3, L2, L3, R3, L2, R1, L4, R5, L1, R5, L2, L1, L5, L2, L5, L2, L4, L2, R3"

class Heading:
    def __init__(self):
        self.d = 0

    def update(self, r_or_l):
        if r_or_l == 'R':
            self.d = (self.d + 1) % 4
        else:
            self.d = (self.d - 1) % 4

    def north(self):
        return self.d == 0

    def east(self):
        return self.d == 1

    def south(self):
        return self.d == 2

    def west(self):
        return self.d == 3


class Location:
    def __init__(self):
        self.x = 0 # like the axes
        self.y = 0
        self.visited = [(0,0)]

    def update(self, heading, distance):
        for d in range(distance):
            if heading.north():
                self.y += 1
            elif heading.east():
                self.x += 1
            elif heading.south():
                self.y -= 1
            elif heading.west():
                self.x -= 1

            new_location = (self.x, self.y)
            if new_location in self.visited:
                print "Already been here!"
                self.visited.append(new_location)
                print "It's {0} blocks away".format(self.distance())
                sys.exit(0)
            else:
                self.visited.append(new_location)

    def distance(self):
        return abs(self.x) + abs(self.y)

heading = Heading()
location = Location()

for step in i.split(', '):
    direction = step[0]
    distance = int(step[1:])

    heading.update(direction)
    location.update(heading, distance)

print location.distance()

