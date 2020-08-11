from random import *
from math import *


def simulated_annealing(population, 
                        initial_temperature, 
                        alpha, 
                        number_of_markov_chains, 
                        length_of_markov_chains, 
                        loop=True):
    def dist(v1, v2):
        return sqrt((v1.x - v2.x) ** 2 + (v1.y - v2.y) ** 2)

    def total_distance(lst):
        d = 0
        for j in range(len(lst) - 1):
            d += dist(lst[j], lst[j + 1])
        return d

    def reverse_sublist(lst, start, end):
        lst[start:end] = lst[start:end][::-1]
        return lst

    temperature = initial_temperature
    path = population.copy()
    if loop:
        path.append(population[0])
    record_distance = total_distance(path)
    for _ in range(number_of_markov_chains):
        temperature *= alpha
        for _ in range(length_of_markov_chains):
            selected_vertices = sample(range(1, len(population) + 1), 2)
            test = path.copy()
            test = reverse_sublist(test, selected_vertices[0], selected_vertices[1])
            test_distance = total_distance(test)
            if test_distance < record_distance:
                record_distance = test_distance
                path = test
            else:
                r = uniform(0, 1)
                if r < exp((record_distance - test_distance) / temperature):
                    record_distance = test_distance
    return path
