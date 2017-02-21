import sys
import datetime
import random
sys.setrecursionlimit(5000000)
file = open(str(sys.argv[1]), "r")
data = file.readlines()
data = map(int, [x.strip() for x in data]) 
# pris de http://rosettacode.org/wiki/Sorting_algorithms/Insertion_sort#Python
def insertion_sort(l):
    for i in xrange(1, len(l)):
        j = i - 1
        key = l[i]
        while (l[j] > key) and (j >= 0):
            l[j + 1] = l[j]
            j -= 1
        l[j + 1] = key
# inspire de http://rosettacode.org/wiki/Sorting_algorithms/Quicksort#Python
def quickSortPivotRandomSeuil(arr, seuil):
    less = []
    pivotList = []
    more = []
    if len(arr) <= 1:
        return arr
    else:
        index = random.randint(0, len(arr) - 1)
        pivot = arr[index]
        for i in arr:
            if i < pivot:
                less.append(i)
            elif i > pivot:
                more.append(i)
            else:
                pivotList.append(i)
        if len(less) >= seuil:
            less = quickSortPivotRandomSeuil(less, seuil)
        else:
            insertion_sort(less)
        if len(more) >= seuil:
            more = quickSortPivotRandomSeuil(more, seuil)
        else:
            insertion_sort(more)
    return less + pivotList + more

seuil = 10

elapsed_time = 0
for x in range(10):
    time_init = datetime.datetime.now()
    result = quickSortPivotRandomSeuil(data, 8)
    time_end = datetime.datetime.now()
    time_delta = time_end - time_init
    elapsed_time = elapsed_time + time_delta.total_seconds()
elapsed_time = elapsed_time / 10

file.close()

if "-p" in sys.argv or "--print" in sys.argv:
    for i in result:
        print i

if "-t" in sys.argv or "--time" in sys.argv:
    print elapsed_time