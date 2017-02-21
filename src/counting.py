# pris de http://rosettacode.org/wiki/Sorting_algorithms/Counting_sort#Python
import sys
import datetime
import numpy
sys.setrecursionlimit(5000000)

file = open(str(sys.argv[1]), "r")
data = file.readlines()
data = map(int, [x.strip() for x in data]) 

def countingSort(array):
    maxval = max(array)
    m = maxval + 1
    count = numpy.bincount(array)
    i = 0
    for a in range(m):  # emit
        for c in range(count[a]):  # - emit 'count[a]' copies of 'a'
            array[i] = a
            i += 1

    return array

time_init = datetime.datetime.now()
result = countingSort(data)
time_end = datetime.datetime.now()
time_delta = time_end - time_init

file.close()

if "-p" in sys.argv or "--print" in sys.argv:
    for i in result:
        print i

if "-t" in sys.argv or "--time" in sys.argv:
    print time_delta.total_seconds()