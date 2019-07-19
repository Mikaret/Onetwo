import math
import stdio
import sys


class Location:

    def __init__(self, lat=0.0, lon=0.0):

        self._lat = lat
        self._lon = lon

    def distanceTo(self, other):

        self._lat = math.radians(self._lat)
        self._lon = math.radians(self._lon)
        other._lat = math.radians(other._lat)
        other._lon = math.radians(other._lon)

        angle1 = math.acos(math.sin(self._lat) * math.sin(other._lat) +
                           math.cos(self._lat) * math.cos(other._lat) *
                           math.cos(self._lon - other._lon))
        angle1 = math.degrees(angle1)
        distance1 = 60.0 * angle1

        # angle1 = math.acos(math.sin(x1) * math.sin(x2) \
        # + math.cos(x1) * math.cos(x2) * math.cos(y1 - y2))

        return distance1

    def __str__(self):

        return '(' + str(self._lat) + ', ' + str(self._lon) + ')'


def _main():
    lat1, lon1, lat2, lon2 = map(float, sys.argv[1:])
    loc1 = Location(lat1, lon1)
    loc2 = Location(lat2, lon2)
    stdio.writeln('loc1 = ' + str(loc1))
    stdio.writeln('loc2 = ' + str(loc2))
    stdio.writeln('d(loc1, loc2) = ' + str(loc1.distanceTo(loc2)))

if __name__ == '__main__':
    _main()
