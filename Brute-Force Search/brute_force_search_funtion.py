from math import *
from itertools import permutations
import sys


def brute_force_search(population):
    
    def dist(v1, v2):
        return sqrt((v1.x - v2.x) ** 2 + (v1.y - v2.y) ** 2)

    def total_distance(lst):
        d = 0
        for j in range(len(lst) - 1):
            d += dist(lst[j], lst[j + 1])
        return d

    if len(population) <= 9:
        paths = permutations(population)
        record_distance = float('inf')
        global record_path
        for path in list(paths):
            if total_distance(path) < record_distance:
                record_distance = total_distance(path)
                record_path = path
        return record_path
    else:
        sys.exit("Error : the size of the population is too large, it must be less than or equal to 9")
