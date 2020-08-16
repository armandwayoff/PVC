from math import *
from random import *
from itertools import permutations
import sys


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


# Note : if 'loop' parameter is set to 'False', the path will start with the first element of the population
def two_opt(population, number_of_markov_chains, loop=True):
    path = population.copy()
    if loop:
        path.append(population[0])
    record_distance = total_distance(path)
    for _ in range(number_of_markov_chains):
        selected_vertices = sample(range(1, len(population) + 1), 2)
        test = path.copy()
        test = reverse_sublist(test, selected_vertices[0], selected_vertices[1])
        test_distance = total_distance(test)
        if test_distance < record_distance:
            record_distance = test_distance
            path = test
    return path


def brute_force_search(population, loop=True):
    global record_path
    if len(population) <= 9:
        if loop:
            paths = []
            for p in list(permutations(population[1:])):
                paths.append((population[0],) + p + (population[0],))
        else:
            paths = permutations(population)
        record_distance = float('inf')
        for path in list(paths):
            if total_distance(path) < record_distance:
                record_distance = total_distance(path)
                record_path = path
        return record_path
    else:
        sys.exit("Error : the size of the population is too large, it must be less than or equal to 9")


def nearest_neighbour(population, starting_vertex):
    visited_vertices = [population[starting_vertex]]
    path = [population[starting_vertex]]
    current_vertex = population[starting_vertex]
    nearest_vertex = current_vertex

    while len(visited_vertices) < len(population):
        record_distance = float('inf')
        for vertex in population:
            if vertex not in visited_vertices:
                d = dist(vertex, current_vertex)
                if d < record_distance:
                    nearest_vertex = vertex
                    record_distance = d
        visited_vertices.append(nearest_vertex)
        path.append(nearest_vertex)
        current_vertex = nearest_vertex
    return path


def simulated_annealing(population,
                        initial_temperature,
                        alpha,
                        number_of_markov_chains,
                        length_of_markov_chains,
                        loop=True):
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
